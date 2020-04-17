#!/usr/bin/env python
# -*- coding:utf-8 -*-

from AppInit import db
from flask_login import UserMixin


class HostUserModel(db.Model, UserMixin):
    __tablename__ = 'ops_host_user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    host_ip = db.Column(db.String(255), unique=True, index=True)
    host_port = db.Column(db.Integer)
    host_user = db.Column(db.String(255))
    host_password = db.Column(db.String(255))
    host_script_path = db.Column(db.String(255))
    host_disk_path = db.Column(db.String(255))

    def __init__(self, host_ip, host_port, host_user, host_password, host_script_path, host_disk_path):
        self.host_ip = host_ip
        self.host_port = host_port
        self.host_user = host_user
        self.host_password = host_password
        self.host_script_path = host_script_path
        self.host_disk_path = host_disk_path

    @staticmethod
    def query_by_hostsID(id):
        return HostUserModel.query.filter(HostUserModel.id == id).first()

    @staticmethod
    def all():
        return HostUserModel.query.all()

    @staticmethod
    def with_entities(*entities):
        return HostUserModel.query.with_entities(*entities)

    def __repr__(self):
        return '<HostInfo:%s>' % self.id

    def add(source):
        db.session.add(source)
        db.session.commit()
