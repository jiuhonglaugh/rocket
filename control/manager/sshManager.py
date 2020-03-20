#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import time
import paramiko

from common.numUtil import randomRandint

sshListDict = {}
sshTimeout = {}


def checkSSH():
    t = []
    for k, v in sshTimeout.items():
        if time.time() > (v + 180):
            t.append(k)
    for i in t:
        sshListDict[i].close()
        del sshListDict[i]
        del sshTimeout[i]


def sshConnect(host, port, username, pwd):
    # 创建ssh链接
    sshclient = paramiko.SSHClient()
    sshclient.load_system_host_keys()
    sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 不限制白名单以外的连接
    try:
        sshclient.connect(host, port, username, pwd)
        chan = sshclient.invoke_shell(term='xterm')  # 创建交互终端
        chan.settimeout(0)
        ids = str(int(time.time() + randomRandint(1, 999999999)))
        sshListDict[ids] = chan
    except paramiko.BadAuthenticationType:
        return json.dumps({'resultCode': 1, 'result': '登录失败,错误的连接类型'})
    except paramiko.AuthenticationException:
        return json.dumps({'resultCode': 1, 'result': '主机认证失败,请检查账号密码'})
    except paramiko.BadHostKeyException:
        return json.dumps({'resultCode': 1, 'result': '登录失败,请检查IP'})
    except:
        return json.dumps({'resultCode': 1, 'result': '登录失败'})
    else:
        sshTimeout[ids] = time.time()
        return json.dumps({'resultCode': 0, 'ids': ids})


def inputCommond(inputStr, ids):
    chan = sshListDict.get(ids)
    sshTimeout[ids] = time.time()
    if not chan:
        return json.dumps({'resultCode': 1})
    chan.send(inputStr)
    return json.dumps({'resultCode': 0})


def getSshStatus(ids):
    chan = sshListDict.get(ids)
    if not chan:
        return json.dumps({'resultCode': 1})
    if not chan.exit_status_ready():
        try:
            data = chan.recv(1024).decode()
        except:
            data = ''
        return json.dumps({'resultCode': 0, 'data': data})
    else:
        chan.close()
        del sshListDict[ids]
        return json.dumps({'resultCode': 1})
