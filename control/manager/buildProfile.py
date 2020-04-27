#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

from common import yml_util
from common.dbUtil import SqlSession
from control.manager.deployManager import getEUP
from common.encryption import b64decode_
from main import config
deployManagerConf = config.getDict('fiel-system')
workPath = deployManagerConf.get('work.path')

def buildWebProfile(inputPath,outPutPath):
    defaultDefaultDict = yml_util.load(inputPath)
    if inputPath.endswith('dev.yml'):
        type = 'mysql'
        user = 'wxgz'
        pwd = 'rocketWeb2020'
        host = '39.107.203.67'
        port = '3306'
        dbName = 'flask'
        uri = "{}+pymysql://{}:{}@{}:{}/{}".format(type, user, pwd, host, port, dbName)
        sqlSession = SqlSession(Uri=uri)
        sql = 'select * from ops_source_detail'
        res = sqlSession.execeQuery(sql=sql)
        for row in res:
            type,host,port,user,pwd,parm = row[1],row[2],row[3],row[4],row[5],row[6]
            print(type,host,port,user,pwd,parm)
            if 'mysql' == type.lower():
                pwd = b64decode_(pwd)
                useAndPwd = getEUP(user,pwd)
                defaultDefaultDict['jasypt']['encryptor']['password'] = useAndPwd.get('password')
                defaultDefaultDict['jasypt']['encryptor']['algorithm'] = useAndPwd.get('algorithm')
                defaultDefaultDict['spring']['datasource']['url'] = '{}://{}:{}{}'.format(type,host,port,parm)
                defaultDefaultDict['spring']['datasource']['username'] = 'ENC({})'.format(useAndPwd.get('user'))
                defaultDefaultDict['spring']['datasource']['password'] = 'ENC({})'.format(useAndPwd.get('pwd'))
            elif 'redis' == type.lower():
                defaultDefaultDict['spring']['redis']['database'] = int(parm)
                defaultDefaultDict['spring']['redis']['password'] = pwd
                if len(host.split(',')) > 1:
                    defaultDefaultDict['spring']['redis']['cluster']['nodes'] = host
                else:
                    hostAndPort = host.split(':')
                    defaultDefaultDict['spring']['redis']['host'] = hostAndPort[0]
                    defaultDefaultDict['spring']['redis']['port'] = int(hostAndPort[1])
            else:
                defaultDefaultDict['elasticsearch_ip'] = host
                defaultDefaultDict['elasticsearch_cluster-name'] = parm
                if user is not None:
                    defaultDefaultDict['xpack.security.user'] = '{}:{}'.format(user,pwd)
                    defaultDefaultDict['xpack.certPath'] = '/home/wxgz/tools/escert'
                else:
                    defaultDefaultDict.pop('xpack.security.user')
                    defaultDefaultDict.pop('xpack.certPath')
        else:
            defaultDefaultDict['server']['port'] = 8098
    yml_util.saveWrite(defaultDefaultDict,outPutPath)



if __name__ == '__main__':
    inputPath = workPath + '/light/infobeat-web/conf/application-dev.yml'
    outPutPath ='C:/Users/MAIBENBEN/Desktop/test.yml'
    buildWebProfile(inputPath,outPutPath)