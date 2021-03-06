#!/usr/bin/env python
# -*- coding:utf-8 -*-
from common.dbUtil import SqlSession, RedisUtil, ElasticsearchUtil

__tableName__ = 'ops_source_detail'

from common.encryption import b64encode_

from control.model.DBSourceModel import DBSourceModel


def testAndSaveMysql(form):
    host = form.mysqlHost.data
    port = form.mysqlPort.data
    user = form.mysqlUser.data
    pwd = form.mysqlPwd.data
    dbName = form.mysqlDbName.data
    parm = form.mysqlParam.data
    type = 'Mysql'
    uri = "mysql+pymysql://{}:{}@{}:{}{}".format(user, pwd, host, port, dbName)
    sqlSession = SqlSession(Uri=uri)
    sql = 'select * from {} where 1=1'.format(__tableName__)
    falg = False
    try:
        sqlSession.execeQuery(sql)
        falg = True
        if not DBSourceModel.query_by_sourceType(type):
            mysqlSource = DBSourceModel(type, host, port, user, b64encode_(pwd), dbName + parm)
            DBSourceModel.add(mysqlSource)
            result = {'code': 200, 'status': '成功', 'message': '成功连接Mysql并保存'}
        else:
            result = {'code': 200, 'status': '失败', 'message': '测试连接成功保存到数据库失败数据库中中已存在mysql数据源'}
    except Exception as e:
        print()
        if falg:
            result = {'code': 201, 'status': '失败', 'message': str(e.with_traceback(None))}
        else:
            result = {'code': 201, 'status': '失败', 'message': str(e.with_traceback(None))}
    return result


def testAndSaveRedis(form):
    host = form.redisHost.data
    pwd = form.redisPwd.data
    dbName = form.redisDbName.data
    type = 'Redis'
    try:
        redisUtil = RedisUtil(host=host, password=pwd, dbName=int(dbName))
        if redisUtil.isAvailable():
            if not DBSourceModel.query_by_sourceType(type):
                redisSource = DBSourceModel(type, host, pwd, dbName)
                DBSourceModel.add(redisSource)
                result = {'code': 200, 'status': '成功', 'message': '成功连接Redis并保存'}
            else:
                result = {'code': 200, 'status': '失败', 'message': '成功连接Redis但未保存，数据库中已存在redis数据源'}
        else:
            result = {'code': 201, 'status': '失败', 'message': str(redisUtil.errorMessage)}
    except Exception as e:
        result = {'code': 201, 'status': '失败', 'message': str(e.with_traceback(None))}
    return result


def testAndSaveEs(form):
    host = form.EsHost.data
    user = form.EsUser.data
    pwd = form.EsPwd.data
    clusterName = form.EsClusterName.data
    type = 'Elasticsearch'
    try:
        es = ElasticsearchUtil(host, user, pwd, clusterName)
        if es.isConn:
            if not DBSourceModel.query_by_sourceType(type):
                esSource = DBSourceModel(type, host, user, pwd, clusterName)
                DBSourceModel.add(esSource)
                result = {'code': 200, 'status': '成功', 'message': 'Elasticsearch集群成功连接并保存'}
            else:
                result = {'code': 200, 'status': '失败', 'message': '成功连接 Elasticsearch 集群但未保存，数据库中已存在 Elasticsearch 数据源'}
        else:
            result = {'code': 201, 'status': '失败', 'message': es.errorMessage}

    except Exception as e:
        result = {'code': 201, 'status': '失败', 'message': str(e.with_traceback(None))}
    return result
