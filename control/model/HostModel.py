#!/usr/bin/env python
# -*- coding:utf-8 -*-

from AppInit import db, sqlSession
from flask_login import UserMixin


class HostModel(db.Model, UserMixin):
    __tablename__ = 'ops_host_detail'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    host_id = db.Column(db.String(255), primary_key=True)
    host_name = db.Column(db.String(255))
    host_ip = db.Column(db.String(255))
    host_total_disk = db.Column(db.String(255))
    host_used_disk = db.Column(db.String(255))
    host_avai_disk = db.Column(db.String(255))
    host_total_memory = db.Column(db.Integer)
    host_free_memory = db.Column(db.Integer)
    host_avai_memory = db.Column(db.Integer)
    host_model_cpu = db.Column(db.String(255))
    host_physical_cpu = db.Column(db.String(255))
    host_logic_cpu = db.Column(db.String(255))
    host_os_time = db.Column(db.String(255))
    host_os_version = db.Column(db.String(255))
    host_computing_time = db.Column(db.String(255))
    update_time = db.Column(db.String(255))

    def __init__(self, id, host_id, host_name, host_ip, host_total_disk,
                 host_used_disk, host_avai_disk, host_total_memory, host_free_memory, host_avai_memory,
                 host_model_cpu, host_physical_cpu, host_logic_cpu, host_os_time, host_computing_time, host_os_version,update_time):
        self.id = id
        self.host_id = host_id
        self.host_name = host_name
        self.host_ip = host_ip
        self.host_total_disk = host_total_disk
        self.host_used_disk = host_used_disk
        self.host_avai_disk = host_avai_disk
        self.host_total_memory = host_total_memory
        self.host_free_memory = host_free_memory
        self.host_avai_memory = host_avai_memory
        self.host_model_cpu = host_model_cpu
        self.host_physical_cpu = host_physical_cpu
        self.host_logic_cpu = host_logic_cpu
        self.host_os_time = host_os_time
        self.host_computing_time = host_computing_time
        self.host_os_version = host_os_version
        self.update_time = update_time

    @staticmethod
    def query_by_hostsID(host_id):
        return HostModel.query.filter(HostModel.host_id == host_id).first()

    @staticmethod
    def all():
        return HostModel.query.all()

    @staticmethod
    def with_entities(*entities):
        return HostModel.query.with_entities(*entities)

    def __repr__(self):
        return '<HostInfo:%s>' % self.id

    def exeSql(sql, echo):
        if echo:
            print(sql)
        return sqlSession.execeQuery(sql)

    def getHostInfo(echo=False):
        sql = '''SELECT host_id,
                        host_ip,
                        host_name,
                        host_total_memory,
                        host_total_disk,
                        host_logic_cpu,
                        host_computing_time,
                        host_os_version FROM {} order by host_id;'''.format(HostModel.__tablename__)
        return HostModel.exeSql(sql, echo)

    def updateHostsDetail(keys, values, echo=False):
        sql = "REPLACE INTO {} ({})VALUES({})".format(HostModel.__tablename__,
                                                      str(keys).replace("'", "").replace('[', '').replace(']', ''),
                                                      str(values).replace('[', '').replace(']', ''))
        HostModel.exeSql(sql, echo)
