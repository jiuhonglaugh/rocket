#!/usr/bin/env python
# -*- coding:utf-8 -*-

from AppInit import db, sqlSession
from flask_login import UserMixin

class DBSourceModel(db.Model, UserMixin):
    __tablename__ = 'ops_source_detail'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    source_type = db.Column(db.String(255))
    source_host = db.Column(db.String(255))
    source_port = db.Column(db.Integer)
    source_user = db.Column(db.String(255))
    source_pwd = db.Column(db.String(255))
    source_parm = db.Column(db.String(255))

    def __init__(self,source_type,source_host,source_port,source_user,source_pwd,source_parm):
        self.source_type = source_type
        self.source_host = source_host
        self.source_port = source_port
        self.source_user = source_user
        self.source_pwd = source_pwd
        self.source_parm = source_parm

    def __init__(self,source_type,source_host,source_pwd,source_parm):
        self.source_type = source_type
        self.source_host = source_host
        self.source_pwd = source_pwd
        self.source_parm = source_parm

    def __init__(self,source_type,source_host,source_user,source_pwd,source_parm):
        self.source_type = source_type
        self.source_host = source_host
        self.source_user = source_user
        self.source_pwd = source_pwd
        self.source_parm = source_parm

    @staticmethod
    def query_by_sourceType(source_type):
        return DBSourceModel.query.filter(DBSourceModel.source_type == source_type).first()

    @staticmethod
    def all():
        return DBSourceModel.query.all()

    @staticmethod
    def with_entities(*entities):
        return DBSourceModel.query.with_entities(*entities)

    def __repr__(self):
        return '<HostInfo:%s>' % self.id

    def exeSql(sql, echo):
        if echo:
            print(sql)
        return sqlSession.execeQuery(sql)

    def add(hostUser):
        db.session.add(hostUser)
        db.session.commit()

