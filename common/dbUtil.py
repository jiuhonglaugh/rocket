#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import sys
from common.configUtil import configUtil
from common.logger import logger

dataBaseList = ['mysql', 'oracle']
parameter = ['db.type', 'db.driver', 'db.host', 'db.user', 'db.passwd', 'db.name']
dicts = configUtil('application.properties').getDict('database')
log = logger('dbUtil')


def checkParameter():
    normal = False
    for key in parameter:
        if dicts.get(key) == '':
            log.error('{} 配置不能为空'.format(key))
            normal = True
    _dbType = dicts.get('db.type')
    if _dbType not in dataBaseList:
        log.error('暂不支持{}数据库，或{}不在数据库列表中，现支持的数据库为：{}'.format(_dbType, _dbType, dataBaseList))
        True

    return normal


def getDBURI():
    if checkParameter():
        sys.exit(1)
    uri = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
        dicts.get('db.type'),
        dicts.get('db.driver'),
        dicts.get('db.user'),
        dicts.get('db.passwd'),
        dicts.get('db.host'),
        dicts.get('db.port'),
        dicts.get('db.name'))
    return uri


if __name__ == '__main__':
    checkParameter()
