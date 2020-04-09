#!/usr/bin/env python
# -*- coding:utf-8 -*-

from AppInit import db, sqlSession
from flask_login import UserMixin


class AgentModel(db.Model, UserMixin):
    __tablename__ = 'ops_host_detail'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    host_id = db.Column(db.String(255))
    host_name = db.Column(db.String(255))
    host_ip = db.Column(db.String(255))
    host_total_disk = db.Column(db.String(255))
    host_used_disk = db.Column(db.String(255))
    host_avai_disk = db.Column(db.String(255))
    host_total_memory = db.Column(db.Integer)
    host_free_memory = db.Column(db.Integer)
    host_used_memory = db.Column(db.Integer)
    host_os_time = db.Column(db.String(255))
    host_computing_time = db.Column(db.String(255))
    update_time = db.Column(db.String(255))

    def __init__(self, id, host_id, host_name, host_ip, host_total_disk,
                 host_used_disk, host_avai_disk, host_total_memory, host_free_memory, host_used_memory,
                 host_computing_time, update_time):
        self.id = id
        self.host_id = host_id
        self.host_name = host_name
        self.host_ip = host_ip
        self.host_total_disk = host_total_disk
        self.host_used_disk = host_used_disk
        self.host_avai_disk = host_avai_disk
        self.host_total_memory = host_total_memory
        self.host_free_memory = host_free_memory
        self.host_used_memory = host_used_memory
        self.host_computing_time = host_computing_time
        self.update_time = update_time

    @staticmethod
    def query_by_hostsID(host_id):
        return AgentModel.query.filter(AgentModel.host_id == host_id).first()

    @staticmethod
    def all():
        return AgentModel.query.all()

    @staticmethod
    def with_entities(*entities):
        return AgentModel.query.with_entities(*entities)

    def __repr__(self):
        return '<HostInfo:%s>' % self.id

    def getHostInfo(echo=False):
        sql = '''SELECT * FROM (
                    SELECT DISTINCT
                        host_id,
                        host_ip,
                        host_name,
                        host_total_memory,
                        host_total_disk,
                        host_physical_cpu,
                        host_computing_time,
                        host_os_version
                    FROM {} ORDER BY update_time DESC) AS s GROUP BY s.host_id;'''.format("ops_host_detail")
        if echo:
            print(sql)
        return sqlSession.execeQuery(sql)
