from django.shortcuts import render
import subprocess
import json
from django.http import JsonResponse
from .management.methods import methods
import time
import random
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import math
# Create your views here.

counter = 0
m = methods()


def demo(request):
    context = {}
    return (render(request, 'demo/vmworld.html', context))

@csrf_exempt
def start(request):
    m.create_fio("192.168.0.102", request.POST, "/dev/sdb")
    m.create_fio("192.168.0.100", request.POST, "/dev/pmem0")
    m.create_fio("192.168.0.101", request.POST, "/dev/pmem0")


    #m.kill_fio("192.168.0.102")
    #m.kill_fio("192.168.0.100")
    # m.kill_fio("192.168.0.101")

    #m.start_fio("192.168.0.102")
    #m.start_fio("192.168.0.100")
    # m.start_fio("192.168.0.101")

    context = {
    }
    return JsonResponse(json.loads(json.dumps(context)))

def shutdown(request):
    m.kill_fio("192.168.0.100")
    m.kill_fio("192.168.0.101")
    m.kill_fio("192.168.0.102")
    context = {
    }
    return JsonResponse(json.loads(json.dumps(context)))

def get_data(request):
    global counter
    counter = counter + 1

    # cpu_util_nvme = m.get_cpu_util('192.168.0.102')
    bw_nvme, iops_nvme, lat_nvme = m.get_data('192.168.0.102')
    bw_nvdimm, iops_nvdimm, lat_nvdimm = m.get_data('192.168.0.100')
    bw_nvdimm2, iops_nvdimm2, lat_nvdimm2 = m.get_data('192.168.0.101')


    context = {
        'nvme_bw': [counter, math.ceil(int(bw_nvme)/1000)],
        'nvme_iops': [counter, int(iops_nvme)],
        'nvme_lat': [counter, (int(lat_nvme)/1000)],
        'nvdimm_bw': [counter, math.ceil(int(bw_nvdimm)/1000)],
        'nvdimm_iops': [counter, int(iops_nvdimm)],
        'nvdimm_lat': [counter, (int(lat_nvdimm)/1000)],
        'nvdimm_bw2': [counter, math.ceil(int(bw_nvdimm2) / 1000)],
        'nvdimm_iops2': [counter, int(iops_nvdimm2)],
        'nvdimm_lat2': [counter, (int(lat_nvdimm2) / 1000)],

    }
    return JsonResponse(json.loads(json.dumps(context)))
