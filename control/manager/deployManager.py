#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from common import timeUtil, exeCmd
from common.SshUtil import SshUtil
from common.dbUtil import SqlSession
from common.encryption import b64decode_
from main import config

deployManagerConf = config.getDict('fiel-system')
workPath = deployManagerConf.get('work.path')


def getEUP(user, pwd):
    fielPath = workPath + '/base/java/cn.infobeat-1.0.jar'
    cmd = 'java -jar -server {} {} {}'.format(fielPath, user, pwd)
    res = exeCmd.Popen(cmd)
    return json.loads(res)


'''
@host       主机地址
@port       主机端口
@user       主机用户
@pwd        主机密码
@localFile  安装包本地路径
@remoteFile 安装包上传路径
@dirPath    安装包解压后的路径
@cmd        执行的安装命令等
@args       执行命令的参数
@removeFile 是否删除安装包  
'''


def installJDK(host, port, user, pwd, localFile, remoteFile, dirPath, cmd, args, removeFile=False):
    print(host, port, user, pwd, path, remoteFile)
    result = dict()
    ssh = True
    ssh = SshUtil(host, user, pwd, port=port, ssh=ssh)
    if ssh.flag:
        if ssh.upLoadFile(localFile, remoteFile):
            timeUtil.sleep(1)
            stdin, stdout, stderr = ssh.exec_commands(cmd, args)
            result[host] = {'success': stdout.read().decode(encoding='utf-8'),
                            'failed': stderr.read().decode(encoding='utf-8')}
            if removeFile and dirPath != '/':
                cmd = 'rm -rf'
                args = '{}*'.format(dirPath)
                ssh.exec_commands(cmd, args)
        else:
            print('上传本地文件 {} 到 {} 服务器 {} 路径失败'.format(localFile, host, remoteFile))
        ssh.close()
    return result


def installInfobratWeb(host, port, user, pwd, localFile, remoteFile, dirPath, cmd, args, removeFile=False):
    print(host, port, user, pwd, path, remoteFile)
    ssh = SshUtil(host, user, pwd, port=port)
    if ssh.flag:
        if ssh.upLoadFile(localFile, remoteFile):
            stdin, stdout, stderr = ssh.exec_commands(cmd, args)
            print(stdout.read().decode(encoding='utf-8'))
            print(stderr.read().decode(encoding='utf-8'))
            if removeFile and dirPath != '/':
                cmd = 'rm -rf'
                args = '{}*'.format(dirPath)
                stdin, stdout, stderr = ssh.exec_commands(cmd, args)
        else:
            print('上传本地文件 {} 到 {} 服务器 {} 路径失败'.format(localFile, host, remoteFile))
        ssh.close()


if __name__ == '__main__':
    # type = 'mysql'
    # user = 'wxgz'
    # pwd = 'rocketWeb2020'
    # host = '39.107.203.67'
    # port = '3306'
    # dbName = 'flask'
    # uri = "{}+pymysql://{}:{}@{}:{}/{}".format(type, user, pwd, host, port, dbName)
    # sqlSession = SqlSession(Uri=uri)
    # sql = 'select * from ops_host_user'
    # res = sqlSession.execeQuery(sql=sql)

    fielPath = workPath + '/base/java/jdk-8.tar.gz'
    host, port, user, pwd, path = '172.10.22.64', 22, 'wxgz', '123456', '/home/wxgz/'  # row[1], row[2], row[3], b64decode_(row[4]), row[6]
    if host == '172.10.22.64':
        remoteFile = path + '/jdk-8.tar.gz'
        dirPath = remoteFile.split('.')[0]
        cmd = 'tar -zxf {} && {}/install_java.sh'.format(remoteFile, dirPath)
        args = '{} {}'.format(path, user)
        res = installJDK(host, port, user, pwd, fielPath, remoteFile, dirPath, cmd, args, True)
        print(json.dumps(res))
