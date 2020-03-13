#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect
from common.dbUtil import getDBURI
from common import timeUtil
db = SQLAlchemy()
app = Flask(__name__)

class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = getDBURI()
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
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
    createApp().run(host='172.10.25.26', port='80')
