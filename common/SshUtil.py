#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import os

import paramiko

# log = Logger(loggername='SshUtil')
from common import fileUtil


class SshUtil:

    def __init__(self, host, userName, passWord, port=22, ssh=True):
        self.__host = host
        self.__port = port
        self.__userName = userName
        self.__passWord = passWord
        if ssh:
            self.__conn = self.__getConnect()

    def __getConnect(self):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.__host, username=self.__userName, password=self.__passWord, port=self.__port,
                        allow_agent=True)
            self.flag = True
            return ssh
        except paramiko.BadAuthenticationType:
            self.flag = False
            self.results = {'code': 201, 'data': '登录失败,错误的连接类型'}
        except paramiko.AuthenticationException:
            self.flag = False
            self.results = {'code': 201, 'data': '主机认证失败,请检查账号密码'}
        except paramiko.BadHostKeyException:
            self.flag = False
            self.results = {'code': 201, 'data': '登录失败,错误的HostKey'}
        except:
            self.flag = False
            self.results = {'code': 201, 'data': '不能连接到主机'}
            return None

    def getMessage(self):
        return self.results

    def exec_commands(self, commond, args):
        'this is use the conn to excute the cmd and return the results of excute the command'
        cmd = '%s %s' % (commond, args)
        return self.__conn.exec_command(cmd)

    def close(self):
        self.__conn.close()

    def upLoadFile(self, localFile, remoteFile):
        if not fileUtil.isFile(localFile):
            return False
        try:
            t = paramiko.Transport((self.__host, self.__port))
            t.connect(username=self.__userName, password=self.__passWord)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.put(localFile, remoteFile)
            return True
        except Exception as e:
            try:
                sftp.mkdir(os.path.split(remoteFile)[0])
                sftp.put(localFile, remoteFile)
                return True
            except Exception:
                return False
            t.close()


if __name__ == '__main__':
    host = '172.10.4.100'
    user = 'wxgz'
    pwd = 'wxgz'
    sshUtil = SshUtil(host=host, userName=user, passWord=pwd)
    stdin, stdout, stderr = sshUtil.exec_commands('/home/wxgz/test.py1', '/home/wxgz/')
    results = stdout.read().decode(encoding='utf-8')
    print(results)
    # results = stdin.read().decode(encoding='utf-8')
    # print(results)
    results = stderr.read().decode(encoding='utf-8')
    print(results)
    #
    # res = json.loads(results)
    # sshUtil.close()
    # print(res.get("DiskUsed"))
