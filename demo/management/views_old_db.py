from django.shortcuts import render
import subprocess
import json
from django.http import JsonResponse
from demo.management.methods import methods
import time
import random
import pandas as pd

# Create your views here.

counter = 0

nvme_prev_io_stall = 0
nvme_prev_num_reads = 0
nvme_prev_num_writes = 0

nvdimm_prev_io_stall = 0
nvdimm_prev_num_reads = 0
nvdimm_prev_num_writes = 0


def demo(request):
    context={}
    return (render(request, 'demo/vmworld.html', context))


def get_data(request):
    global counter

    global nvme_prev_io_stall
    global nvme_prev_num_reads
    global nvme_prev_num_writes
    
    global nvdimm_prev_io_stall
    global nvdimm_prev_num_reads
    global nvdimm_prev_num_writes


    counter = counter + 1

    m = methods()
    tps_nvme = m.get_tps('192.168.0.103')
    tpm_nvme = m.get_tpm('192.168.0.103')

    cpu_util_nvme = m.get_cpu_util('192.168.0.102')

    nvme_io_stall, nvme_num_reads, nvme_num_writes = m.get_latency('192.168.0.102')

    shadow = nvme_io_stall
    nvme_io_stall = nvme_io_stall-nvme_prev_io_stall
    nvme_prev_io_stall = shadow

    shadow = nvme_num_reads
    nvme_num_reads = nvme_num_reads-nvme_prev_num_reads
    nvme_prev_num_reads = shadow

    shadow = nvme_num_writes
    nvme_num_writes = nvme_num_writes-nvme_prev_num_writes
    nvme_prev_num_writes = shadow

    try:
        nvme_latency = (round(nvme_io_stall/(nvme_num_reads+nvme_num_writes),2))
    except:
        nvme_latency = ""

    tps_nvdimm = m.get_tps('192.168.0.101')
    tpm_nvdimm = m.get_tpm('192.168.0.101')

    cpu_util_nvdimm = m.get_cpu_util('192.168.0.100')

    nvdimm_io_stall, nvdimm_num_reads, nvdimm_num_writes = m.get_latency('192.168.0.100')

    shadow = nvdimm_io_stall
    nvdimm_io_stall = nvdimm_io_stall-nvdimm_prev_io_stall
    nvdimm_prev_io_stall = shadow

    shadow = nvdimm_num_reads
    nvdimm_num_reads = nvdimm_num_reads-nvdimm_prev_num_reads
    nvdimm_prev_num_reads = shadow

    shadow = nvdimm_num_writes
    nvdimm_num_writes = nvdimm_num_writes-nvdimm_prev_num_writes
    nvdimm_prev_num_writes = shadow

    try:
        nvdimm_latency = (round(nvdimm_io_stall/(nvdimm_num_reads+nvdimm_num_writes),2))
    except:
        nvdimm_latency = ""


    context = {
        'nvme_tps': [counter, tps_nvme],
        'nvme_tpm': tpm_nvme,
        'nvme_cpu': [counter, cpu_util_nvme],
        'nvme_lat': [counter, nvme_latency],
        'nvdimm_tps': [counter, tps_nvdimm],
        'nvdimm_tpm': tpm_nvdimm,
        'nvdimm_cpu': [counter, cpu_util_nvdimm],
        'nvdimm_lat': [counter, nvdimm_latency],
    }
    return JsonResponse(json.loads(json.dumps(context)))