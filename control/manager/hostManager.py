#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import random
import time

from common import ModelUtil
from common.SshUtil import SshUtil
from common.encryption import b64encode_
from common.numUtil import randomRandint
from common.timeUtil import getTime, formatTime
from control.model.HostModel import HostModel
from control.model.HostUserModel import HostUserModel
from common.Logger import Logger
from main import config

hostManagerConf = config.getDict('fiel-system')
log = Logger(loggername='hostManager')


def getHostsDetail(isLine):
    result = HostModel.getHostInfo()
    dtList = ModelUtil.toDictAll(result)
    nowTime = formatTime(timestamp=time.time(), reduce=10)
    for i in range(len(dtList) - 1, -1, -1):
        if str(dtList[i]['host_computing_time']) > nowTime:
            dtList[i]['host_status'] = 'online'
        else:
            dtList[i]['host_status'] = 'offline'
        if isLine == "1" and dtList[i]['host_status'] == 'offline':
            dtList.pop(i)
        elif isLine == "2" and dtList[i]['host_status'] == 'online':
            dtList.pop(i)
    return dtList


def hostAdd(form):
    host_ip = form.host_ip.data
    host_script_path = form.host_script_path.data
    host_user = form.host_user.data
    host_port = form.host_port.data
    host_password = form.host_password.data
    host_disk_path = form.host_disk_path.data
    sshUtil = SshUtil(host=host_ip, port=host_port, userName=host_user, passWord=host_password)
    if not sshUtil.flag:
        return sshUtil.getMessage()
    localFile = hostManagerConf.get('work.path') + '/light/agent/collection/agent.py'
    flag = sshUtil.upLoadFile(localFile, host_script_path)
    if flag:
        sshUtil.exec_commands('chmod +x ', host_script_path)
        hostUser = HostUserModel(host_ip, host_port, host_user, b64encode_(host_password), host_script_path,
                                 host_disk_path)
        HostUserModel.add(hostUser)
        return json.dumps({'code': 200, 'status': 'Success', 'message': '{}主机添加成功'.format(host_ip)})
    return json.dumps({'code': 201, 'status': 'Failed', 'message': '{}文件可能不存在或不是文件请查看后台日志'.format(localFile)})


def getHostInfo(hostId):
    res = HostModel.query_by_hostsID(hostId)
    if res is not None:
        result = ModelUtil.toDict(res, res.__class__)
        return result
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
