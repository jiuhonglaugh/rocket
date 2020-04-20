#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import sys
import redis
from rediscluster import RedisCluster
from sqlalchemy.dialects.mysql import pymysql
from common.ConfigUtil import ConfigUtil
from common.Logger import Logger
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

dataBaseList = ['mysql', 'oracle']
parameter = ['db.type', 'db.driver', 'db.host', 'db.user', 'db.passwd', 'db.name']
dicts = ConfigUtil('application.properties').getDict('database')
log = Logger('dbUtil')


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


def testConnMysql(host, port):
    conn = pymysql.connect(
        host="你的数据库地址",
        user="用户名",
        password="密码",
        database="数据库名",
        charset="utf8")


class SqlSession:
    # 创建会话
    def __init__(self, Uri=getDBURI()):
        # 创建数据库引擎
        # 细节1  sqlalchemy默认实现了连接池功能, 并且可以自动重连(pool_size 连接池中的连接数, max_overflow 超出连接池的额外连接数)
        # 细节2  如果数据库使用utf-8支持中文, 则设置连接地址时需要标明  ?charset=utf8   否则报错
        engine = create_engine(Uri, echo=False, pool_size=5, max_overflow=10)
        """封装Session创建过程   此函数只在应用初始化时调用一次即可"""
        # 创建Session工厂     SessionFactory()就可以创建出session对象, 但是该对象没有实现线程隔离
        SessionFactory = sessionmaker(bind=engine)
        # 生成线程隔离的session对象(每个线程取自己的session)
        self.session = scoped_session(SessionFactory)
        # ps: 其实返回的session是scoped_session类型对象, 再通过session()才会创建Session对象, 不过scoped_session实现了代理功能, 进行数据操作时, 会自动创建/获取实现了线程隔离的Session对象并执行操作

    @contextmanager  # 装饰器形式的上下文管理器
    def __session_scope(self):
        """使用上下文管理器对session和事务操作进行封装"""
        try:
            yield self.session
            self.session.commit()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.remove()  # session工作完成, 销毁session, 释放内存

    def execeQuery(self, sql):
        with self.__session_scope() as session:  # 获取session对象, 代码块执行完会自动提交 并 销毁session
            return session.execute(sql)


class RedisUtil:
    def __init__(self, host, password, dbName):
        self.host = host
        self.password = password
        self.dbName = dbName
        self.redisNodes = []

    def __isCluster(self):
        clusterHost = self.host.split(',')
        if len(clusterHost) > 1:
            for node in clusterHost:
                self.redisNodes.append({node.split(':')[0]: int(node.split(':')[1])})
            return True
        return False

    def getConn(self):
        if self.__isCluster():
            return self.__getRedisClusterConn()
        else:
            return self.__getRedisConn()

    def __getRedisClusterConn(self):
        try:
            return RedisCluster(startup_nodes=self.redisNodes, password=self.password, decode_responses=True)
        except Exception as e:
            print(e.with_traceback(None))

    def __getRedisConn(self):
        hostAndPort = self.host.split(':')
        host = hostAndPort[0]
        port = int(hostAndPort[1])
        return redis.Redis(host=host, port=port, password=self.password, db=self.dbName)

    def isAvailable(self):
        try:
            self.getConn().get('aa')
            return True
        except Exception as e:
            self.errorMessage = e.with_traceback(None)
        return False


if __name__ == '__main__':
    host = '172.10.10.120:9000,172.10.10.121:9001,172.10.10.122:9001'
    auth = '4rGhQpgkPRzS'
    redisUtil = RedisUtil(host, auth, 1)
    if redisUtil.isAvailable():
        print(True)
    else:
        print(redisUtil.errorMessage)
