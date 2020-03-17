#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect
from common.dbUtil import getDBURI
from common import timeUtil
from common import ConfigUtil

db = SQLAlchemy()
app = Flask(__name__)
config = ConfigUtil.ConfigUtil('application.properties').getDict('rocket')


class Config:
    SECRET_KEY = 'hard to guess string'
    '''
    1.数据库地址，用户，密码，数据库名称
    2.动态跟踪修改如果设置为True会影响执行效率
    3.自动提交
    4.数据库连接回收时间
    5.数据库连接池大小
    6.打印执行的sql脚本
    7.session过期时间
    8.是否打卡idebug 模式
    '''
    SQLALCHEMY_DATABASE_URI = getDBURI()
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_POOL_RECYCLE = 10
    SQLALCHEMY_POOL_SIZE = 30
    SQLALCHEMY_ECHO = False
    PERMANENT_SESSION_LIFETIME = timeUtil.sessionTimeOut(minutes=15)
    DEBUG = True


def reisterBluePrint(app):
    from control.views.loginBlue import login_blue
    from control.views.hostBlue import hostInfo_blue
    from control.views.manager import manager_blue
    app.register_blueprint(login_blue, ull_prefix='/')
    app.register_blueprint(hostInfo_blue, ull_prefix='/host')
    app.register_blueprint(manager_blue, ull_prefix='/host')


def createApp():
    reisterBluePrint(app)
    app.config.from_object(Config)  # 这里在初始化db之前需要先加载配置文件，问题解决
    csrf = CsrfProtect()
    csrf.init_app(app)
    db.init_app(app)
    return app


if __name__ == '__main__':
    host = config.get('rocket.host')
    port = config.get('rocket.port')
    createApp().run(host=host, port=port)
