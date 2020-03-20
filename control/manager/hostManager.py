#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

from common import ModelUtil, timeUtil
from common.numUtil import is_number, randomRandint
from common.timeUtil import getTime
from model.HostModel import HostInfoModel


def getHostsInfo(isLine):
    result = HostInfoModel.query.with_entities(HostInfoModel.id, HostInfoModel.host_name,
                                               HostInfoModel.host_total_memory, HostInfoModel.host_ip,
                                               HostInfoModel.host_total_cpu, HostInfoModel.host_total_disk,
                                               HostInfoModel.update_time)
    dtList = ModelUtil.toDictAll(result)
    for i in range(len(dtList) - 1, -1, -1):
        dtList[i]['host_os'] = 'CentOS Linux release 7.7.1908 (Core)'
        if str(dtList[i]['update_time']) > timeUtil.getTime(reduce=10):
            dtList[i]['status'] = 'online'
        else:
            dtList[i]['status'] = 'offline'
        if isLine == "1" and dtList[i]['status'] == 'offline':
            dtList.pop(i)
        elif isLine == "2" and dtList[i]['status'] == 'online':
            dtList.pop(i)
    return dtList


def getHostInfo(hostId):
    if is_number(hostId):
        res = HostInfoModel.query_by_hostsID(hostId)
        if res is not None:
            result = ModelUtil.toDict(res, res.__class__)
            result['host_os'] = 'CentOS Linux release 7.7.1908 (Core)'
            return result
        return None
    return None





def getData():
    return [random.randint(50, 99), random.randint(50, 99), random.randint(50, 99), random.randint(50, 99),
            random.randint(50, 99), random.randint(50, 99), random.randint(50, 99),
            random.randint(50, 99), random.randint(50, 99), random.randint(50, 99)]


def getCore():
    title = ['hadoop01', 'hadoop02', 'hadoop03', 'hadoop04', 'hadoop05']
    time = [getTime(format='%H:%M:%S', reduce=30), getTime(format='%H:%M:%S', reduce=25),
            getTime(format='%H:%M:%S', reduce=20), getTime(format='%H:%M:%S', reduce=15),
            getTime(format='%H:%M:%S', reduce=10), getTime(format='%H:%M:%S', reduce=10),
            getTime(format='%H:%M:%S', reduce=5), getTime(format='%H:%M:%S'),
            getTime(format='%H:%M:%S', reduce=5), getTime(format='%H:%M:%S')]
    jsondata = {'title': title, 'time': time}
    data = []
    for node in title:
        data.append({'name': node, 'type': 'line', 'stack': '总量', 'data': getData()})
    jsondata['data'] = data
    return jsondata


def getMem():
    x = []
    y = []
    x.append('hadoop01')
    y.append(randomRandint())
    x.append('hadoop01')
    y.append(randomRandint())
    x.append('hadoop03')
    y.append(randomRandint())
    x.append('hadoop04')
    y.append(randomRandint())
    x.append('hadoop05')
    y.append(randomRandint())
    jsondata = {}
    jsondata['xdays'] = x
    jsondata['yvalues'] = y
    return jsondata


'''
折线图需要三种数据
第一 title 对应折线图上方显示的 标题数据
第二 time  对应折线图下方显示的 时间数据
第三 data  对应折现图中显示的   结果数据
time 和 data 中的数据数量一致否则显示会缺失
'''


def getNet():
    title = ['hadoop01', 'hadoop02', 'hadoop03', 'hadoop04', 'hadoop05']
    time = [getTime(format='%H:%M:%S', reduce=30), getTime(format='%H:%M:%S', reduce=25),
            getTime(format='%H:%M:%S', reduce=20), getTime(format='%H:%M:%S', reduce=15),
            getTime(format='%H:%M:%S', reduce=10), getTime(format='%H:%M:%S', reduce=10),
            getTime(format='%H:%M:%S', reduce=5), getTime(format='%H:%M:%S'),
            getTime(format='%H:%M:%S', reduce=5), getTime(format='%H:%M:%S')]
    jsondata = {'title': title, 'time': time}
    data = []
    for node in title:
        data.append({'name': node, 'type': 'line', 'stack': '总量', 'data': getData()})
    jsondata['data'] = data
    return jsondata


def getDisk():
    x = []
    y = []
    x.append('hadoop01')
    y.append(randomRandint(40, 50))
    x.append('hadoop01')
    y.append(randomRandint(40, 50))
    x.append('hadoop03')
    y.append(randomRandint(40, 50))
    x.append('hadoop04')
    y.append(randomRandint(40, 50))
    x.append('hadoop05')
    y.append(randomRandint(40, 50))
    jsondata = {}
    jsondata['xdays'] = x
    jsondata['yvalues'] = y
    return jsondata
