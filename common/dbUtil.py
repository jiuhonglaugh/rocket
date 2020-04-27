#!/usr/bin/python3
# -*- encoding:utf-8 -*-
import json
import sys
import redis
from elasticsearch import Elasticsearch
from rediscluster import RedisCluster
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


class ElasticsearchUtil:
    """
    sniff_on_start  启动前嗅探es集群服务器

    """

    def __init__(self, host, user, pwd, clusterName):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.clusterName = clusterName
        self.isConn = False
        self.__conn = self.__ConnEs()

    def __ConnEs(self):
        try:
            conn = Elasticsearch(self.host.split(','), http_auth=(self.user, self.pwd), sniff_on_start=True,
                                 sniff_on_connection_fail=True, sniffer_timeout=60)
            self.isConn = True
            return conn
        except Exception as e:
            self.errorMessage = str(e.with_traceback(None))
        return None

    def getClusterHealth(self):
        return json.dumps(self.__conn.cluster.health())

    def getClusterStats(self):
        return json.dumps(self.__conn.cluster.stats())

    def catClusterNodes(self):
        return self.__conn.cat.nodes()


if __name__ == '__main__':
    host = '172.10.4.100:9200,172.10.4.101:9200,172.10.4.102:9200'
    user = 'elastic'
    pwd = 'infobeat123'
    clusterName = 'infobeat123'
    es = ElasticsearchUtil(host, user, pwd, clusterName)
    if es.isConn:
        print(es.getClusterHealth())
    else:
        print(es.errorMessage)
