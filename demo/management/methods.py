import pexpect
import subprocess
import pandas as pd
import paramiko
import os

class methods():
    def __int__(self):
        pass

    def start_fio(self, ipaddress):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ipaddress, username="micron", password="micron")
        cmd = '\"/home/micron/run.sh\"'
        ssh.exec_command(cmd)


    def kill_fio(self, ipaddress):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ipaddress, username="micron", password="micron")
        cmd = '\"/home/micron/kill.sh\"'
        ssh.exec_command(cmd)

    def get_data(self, ipaddress):
        cmd = 'sqlcmd -S '+ipaddress+' -U SA -P Micron18! -m 1 -Q \"SET NOCOUNT ON; USE fio; SELECT top(1) * FROM FioData;\"'
        result = subprocess.check_output(cmd, shell=True)
        result = result.decode("utf-8")
        result = result.split("\n")
        result = list(filter(None, result))[-1]
        result = list(filter(None, result.split(" ")))

        # Empty. Return 0.
        if result[0] == "-----------":
            return 0, 0, 0
        # Has data. Delete entry and pass values to gui.
        else:
            cmd = 'sqlcmd -S '+ipaddress+' -U SA -P Micron18! -m1 -Q \"SET NOCOUNT ON; USE fio; DELETE top(SELECT COUNT(1)) FROM FioData;\"'
            os.system(cmd)
            # bw, iops, lat
            return result[1], result[2], result[3]

    def create_fio(self, ipaddress, parameters, drive_name):
        operation_array = ["read", "write", "randread", "randwrite"]

        fio_defaults = {
            "direct": 1,
            'randrepeat': 0,
            'ioengine': 'libaio',
            'time_based': 1,
            'runtime': 160,
            'size': '12G',
            'group_reporting': 1,
            'ramp_time': 10,
            'rw': 'randwrite',
            'bs': '4k',
            'rwmixread': 0,
            'rwmixwrite': 100,
            'filename': drive_name,
            'thread': 8,
            'numjobs': 8,
            'iodepth': 8,
            'loops': 100,
            'write_bw_log': "bw",
            'write_iops_log': "iops",
            'write_lat_log': "lat",
            'log_avg_msec': 1000,
        }

        new_fio = fio_defaults
        new_fio["bs"] = str(parameters["bs"])+"k"
        new_fio["size"] = str(parameters["size"])+"G"
        new_fio["numjobs"] = parameters["numjobs"]
        new_fio["iodepth"] = parameters["numjobs"]
        new_fio["thread"] = parameters["numjobs"]
        new_fio["rw"] = operation_array[int(parameters["rw"])]
        new_fio["rwmixread"] = parameters["rwmixread"]
        new_fio["rwmixwrite"] = parameters["rwmixwrite"]
        new_fio["runtime"] = parameters["runtime"]

        path = os.path.dirname(os.path.realpath(__file__))
        fio_file_name = path + "/my_fio.fio"
        f = open(fio_file_name, 'w')
        start = "[global]\n"
        end = "[finish-test]"
        f.write(start)
        for key, val in new_fio.items():
            f.write("" + key + "=" + str(val) + "\n")
        f.write(end)
        f.close()


        cmd = "scp "+path+"/my_fio.fio micron@"+ipaddress+":/home/micron/fio_testing/"
        ssh_newkey = 'Are you sure you want to continue connecting'
        p = pexpect.spawn(cmd)
        i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])

        if i == 0:
            p.sendline('yes')
            i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])
        if i == 1:
            p.sendline('micron')
            i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])
        if i == 3:
            pass


    def get_cpu_util(self, ipaddress):
        ssh_newkey = 'Are you sure you want to continue connecting'
        p = pexpect.spawn('ssh micron@'+ipaddress+' sar 1 1')
        i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])

        if i == 0:
            p.sendline('yes')
            i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])
        if i == 1:
            p.sendline('micron')
            i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])
        if i == 3:
            pass

        cpu_data = p.before
        cpu_data = cpu_data.decode("utf-8")
        cpu_data = cpu_data.replace(" ",",").replace("\n","").replace("\r","").replace("\t","")
        cpu_data = cpu_data.split(",")
        cpu_data = list(filter(None, cpu_data))

        return (round(100 - float(cpu_data[21].replace("Average:","")),2))

    # def get_latency(self, ipaddress):
    #     cmd = 'sqlcmd -S '+ipaddress+' -U SA -P Micron18! -i /home/micron/vmware_demo/demo/management/latency.sql'
    #     data = subprocess.check_output(cmd, shell=True)
    #     data = data.decode("utf-8")
    #     data = data.replace("-","")
    #     data = data.replace("\n","")
    #     data = data.split(" ")
    #     data = list(filter(None, data))
    #
    #     new_data = []
    #     temp_arr = []
    #     for n,x in enumerate(data):
    #         if n%8==0:
    #             if temp_arr:
    #                 new_data.append(temp_arr)
    #             temp_arr = []
    #             temp_arr.append(x)
    #         else:
    #             temp_arr.append(x)
    #
    #     df = pd.DataFrame(new_data[1:])
    #     df.columns = new_data[0]
    #     df = df[df["DB"]=='tpcc250'].iloc[[0]]
    #
    #     return int(df['io_stall']), int(df['num_of_reads']), int(df['num_of_writes'])
    #
    # def get_tps(self, ipaddress):
    #     ssh_newkey = 'Are you sure you want to continue connecting'
    #     p = pexpect.spawn('ssh micron@'+ipaddress+' cat /home/micron/data.txt')
    #     i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])
    #
    #     if i == 0:
    #         p.sendline('yes')
    #         i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])
    #     if i == 1:
    #         p.sendline('micron')
    #         i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])
    #     if i == 3:
    #         pass
    #
    #     tps_data = p.before
    #     tps_data = tps_data.decode("utf-8")
    #     tps_data = tps_data.replace("\n",'').replace("\r",'')
    #     return int(tps_data)
    #
    # def get_tpm(self, ipaddress):
    #     ssh_newkey = 'Are you sure you want to continue connecting'
    #     p = pexpect.spawn('ssh micron@' + ipaddress + ' cat /home/micron/tpm.txt')
    #     i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])
    #
    #     if i == 0:
    #         p.sendline('yes')
    #         i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])
    #     if i == 1:
    #         p.sendline('micron')
    #         i = p.expect([ssh_newkey, '.*password.*', pexpect.EOF])
    #     if i == 3:
    #         pass
    #
    #     tpm_data = p.before
    #     tpm_data = tpm_data.decode("utf-8")
    #     tpm_data = tpm_data.replace("\n",'').replace("\r",'')
    #     return int(tpm_data)
