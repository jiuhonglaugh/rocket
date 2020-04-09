#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import json
import subprocess as sub
import socket
import re
import sys
import time

dt = dict()


def getHostIp():
    ip = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]

    finally:
        dt["host_ip"] = ip
        s.close()


def execeComm(commond):
    res = sub.Popen(commond, shell=True, stdout=sub.PIPE)
    res.wait()
    return res


def getMem():
    commond = 'cat /proc/meminfo | grep -E "MemAvailable|MemTotal|MemFree"'
    res = execeComm(commond)
    result = res.stdout.read().replace(' ', '')
    for line in result.split('\n'):
        data = line.split(':')
        if len(data) == 2:
            if data[0] == "MemTotal":
                dt['host_total_memory'] = int(data[1].strip()[:-2])
            if data[0] == "MemAvailable":
                dt['host_avai_memory'] = int(data[1].strip()[:-2])
            if data[0] == "MemFree":
                dt['host_free_memory'] = int(data[1].strip()[:-2])


def getCpu():
    commond = 'cat /proc/cpuinfo | grep "processor" | wc -l'
    res = execeComm(commond)
    dt['host_logic_cpu'] = res.stdout.read().strip()
    commond = 'cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l'
    res = execeComm(commond)
    dt['host_physical_cpu'] = res.stdout.read().strip()
    commond = 'cat /proc/cpuinfo | grep name |cut -f2 -d: | uniq'
    res = execeComm(commond)
    dt['host_model_cpu'] = res.stdout.read().strip()


def getCpuUsage():
    commond = "top -b -n 1 | awk '{print $9}'"
    lines = execeComm(commond).stdout.read().strip().split('\n')
    cpu_usage = 0.00
    for line in lines[7:]:
        cpu_usage += float(line)
    cpu_usage /= int(dt['LogicCore'])
    dt['UsageCore'] = cpu_usage


def getDisk(path):
    commond = "df -h {} | sed -n '2p'".format(path)
    res = execeComm(commond).stdout.read().strip()
    group = re.findall(r"\d+\.?\d*", res)
    dt['host_total_disk'] = float(group[0])
    dt['host_used_disk'] = float(group[1])
    dt['host_avai_disk'] = float(group[2])


def getHostName():
    commond = 'cat /etc/hostname'
    res = execeComm(commond)
    dt['host_name'] = res.stdout.read().strip()


def getOsInfo():
    commond = 'cat /etc/redhat-release'
    res = execeComm(commond)
    dt['host_os_version'] = res.stdout.read().strip()


def getOSTime():
    dt['host_os_time'] = time.time()


def getHostID():
    data = dt['host_name'] + dt['host_ip']
    md5Id = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()[:5]
    dt['host_id'] = md5Id


if __name__ == '__main__':

    getHostIp()
    getMem()
    getCpu()
    getOsInfo()
    getHostName()
    getOSTime()
    getHostID()
    if len(sys.argv) > 1:
        getDisk(sys.argv[1])
        print(json.dumps(dt))
    else:
        getDisk('~')
        print(json.dumps(dt))
