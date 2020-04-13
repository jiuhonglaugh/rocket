#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import random
import time
from common.SshUtil import SshUtil
from common.encryption import b64decode_
from control.model.HostModel import HostModel
from control.model.HostUserModel import HostUserModel
from common import ModelUtil
from common.timeUtil import formatTime


def getAgentHostDetail():
    result = dict()
    nodes = HostModel.query.with_entities(HostUserModel.host_ip, HostUserModel.host_port,
                                          HostUserModel.host_user, HostUserModel.host_password,
                                          HostUserModel.host_script_path, HostUserModel.host_disk_path)
    jsonList = ModelUtil.toJsonAll(nodes)

    initTime = 0.000
    for node in jsonList:
        info = json.loads(node)
        host = info.get('host_ip')
        port = info.get('host_port')
        userName = info.get('host_user')
        passWord = b64decode_(info.get('host_password'))
        script_path = info.get('host_script_path')
        disk_path = info.get('host_disk_path')
        startTime = time.time()
        sshUtil = SshUtil(host=host, port=port, userName=userName, passWord=passWord)
        if sshUtil.flag:
            stdin, stdout, stderr = sshUtil.exec_commands(script_path, disk_path)
            endTime = time.time()
            results = stdout.read().decode(encoding='utf-8').replace("'", "\"")
            if results != '':
                res = json.loads(results)
                tmpTime = endTime - startTime
                computingTime = res.get('host_os_time') - (tmpTime + initTime)
                res.update({'host_computing_time': formatTime(timestamp=computingTime)})
                res.update({'host_os_time': formatTime(timestamp=res.get('host_os_time'))})
                initTime += tmpTime
                sshUtil.close()
                keys = []
                vals = []
                for key, val in res.items():
                    keys.append(key)
                    vals.append(val)
                if len(keys) > 2 and len(vals) > 2:
                    HostModel.updateHostsDetail(keys=keys, values=vals)
                result[host] = 'Success'
            else:
                result[host] = {'status': 'Failed', 'message': stderr.read().decode(encoding='utf-8')}
        else:
            result[host] = {'status': 'Failed', 'message': sshUtil.getMessage()}
    return json.dumps(result)


def agentTestConn(form):
    host_ip = form.host_ip.data
    host_script_path = form.host_script_path.data
    host_user = form.host_user.data
    host_port = form.host_port.data
    host_password = form.host_password.data
    tmpFile = host_script_path + '_bak'
    sshUtil = SshUtil(host=host_ip, port=host_port, userName=host_user, passWord=host_password)
    if not sshUtil.flag:
        return sshUtil.getMessage()
    stdin, stdout, stderr = sshUtil.exec_commands('touch', tmpFile)
    errStr = stderr.read().decode(encoding='utf-8')
    if errStr is not "":
        return {'code': 201, 'data': errStr}
    sshUtil.exec_commands('rm -rf', tmpFile)
    sshUtil.close()
    return {'code': 200, 'data': 'success'}
