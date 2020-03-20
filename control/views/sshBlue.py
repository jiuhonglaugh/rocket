#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from flask import request, render_template, Blueprint
from common.form import SshForm
from control.manager.loginManager import cklogin
from control.manager.sshManager import sshConnect, inputCommond, getSshStatus
from AppInit import csrf
ssh_blue = Blueprint('ssh', __name__)
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


@ssh_blue.route('/ssh/login')
def index():
    form = SshForm()
    return render_template('webssh.html', form=form)


# 此方法用于处理ssh登陆,并返回id号码
@ssh_blue.route('/ssh/connect', methods=['POST'])
def ssh():
    form = SshForm(request.form)
    host = form.host.data
    port = form.port.data
    username = form.username.data
    pwd = form.pwd.data
    result = sshConnect(host, port, username, pwd)
    return result


# 此方法用于获取前端监听的键盘动作,输入到远程ssh
@csrf.exempt
@ssh_blue.route('/ssh/sshInput', methods=['POST'])
def sshInput():
    WebInput = request.values.get('input')
    ids = request.values.get('ids')
    result = inputCommond(WebInput, ids)
    return result


# 根据id号,获取远程ssh结果,方法比较low,用的轮询而没有用socket
@csrf.exempt
@ssh_blue.route('/ssh/getSsh', methods=['POST'])
def getSsh():
    ids = request.values.get('ids')
    result = getSshStatus(ids)
    return result


# 批量远程主机执行shell
@ssh_blue.route('/ssh/batchExec', methods=['GET', 'POST'])
@cklogin()
def batchExec():
    if request.method == 'GET':
        return render_template('batchExec.html')

# 添加主机
# @app.route('/ssh/createBatchExec', methods=['POST'])
# @cklogin()
# def createBatchExec():
#     IP = request.values.get('IP')
#     PORT = request.values.get('PORT')
#     PWD = request.values.get('PWD')
#     GROUPS = request.values.get('GROUPS')
#     NOTE = request.values.get('NOTE')
#     USERNAME = request.values.get('USERNAME')
#     ROOTPWD = request.values.get('ROOTPWD')
#     if not (IP and PWD and USERNAME):
#         return json.dumps({'resultCode': 1, 'result': '请输入正确的IP和账号密码'})
#     sqlResult = sql.insertRemoteHost(IP=IP, PORT=PORT, CTYPE='PWD', USERNAME=USERNAME, GROUPS=GROUPS, NOTE=NOTE,
#                                      PWD=PWD, PKPATH=None, ROOTPWD=ROOTPWD)
#     if sqlResult[0]:
#         return json.dumps({'resultCode': 0})
#     else:
#         return json.dumps({'resultCode': 1, 'result': str(sqlResult[1])})


# # 查询主机
# @app.route('/SelectBatchExec', methods=['POST'])
# @cklogin()
# def SelectBatchExec():
#     sqlResult = sql.selectRemoteHost()
#     if sqlResult[0]:
#         return json.dumps({'resultCode': 0, 'result': list(sqlResult[1])})
#     else:
#         return json.dumps({'resultCode': 1, 'result': str(sqlResult[1])})


# # 删除主机
# @app.route('/DeletetBatchExec', methods=['POST'])
# @cklogin()
# def DeletetBatchExec():
#     ipList = json.loads(request.values.get('ipList'))
#     for i in ipList:
#         sqlResult = sql.deleteRemoteHost(i)
#         if not sqlResult[0]:
#             return json.dumps({'resultCode': 1, 'result': str(sqlResult[1])})
#     return json.dumps({'resultCode': 0})


# 执行远程SHELL
# @app.route('/BatchExecShell', methods=['POST'])
# @cklogin()
# def BatchExecShell():
#     ipList = json.loads(request.values.get('ipList'))
#     shell = request.values.get('shell')
#     userRoot = (True if shell[-5:] == '#root' else False)
#     if userRoot:
#         shell = shell[:-5]
#     for i in ipList:
#         sqlResult = sql.selectRemoteHostForIP(i)
#         if not sqlResult[0]:
#             return json.dumps({'resultCode': 1, 'result': str(sqlResult[1])})
#         else:
#             ssh = paramiko.SSHClient()
#             ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#             ip = sqlResult[1][0]
#             port = sqlResult[1][1]
#             username = sqlResult[1][2]
#             pwd = sqlResult[1][3]
#             rootpwd = sqlResult[1][4]
#             ssh.connect(ip, int(port), username, pwd)
#             if userRoot:
#                 # 如果以root身份运行shell,先su并回车,输入密码,再执行shell
#                 std_in, std_out, std_err = ssh.exec_command('su' + '\n', get_pty=True)
#                 std_in.write(rootpwd + '\n')
#                 std_in.write(shell + '\n')
#             else:
#                 ssh.exec_command(shell + '\n', get_pty=True)
#             ssh.close()
#     return json.dumps({'resultCode': 0})
