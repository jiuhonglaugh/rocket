#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, url_for

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

from common.dbUtil import getDBURI


class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_DATABASE_URI = getDBURI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True


db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)  # 这里在初始化db之前需要先加载配置文件，问题解决
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return '账号或密码不能为空', 202
    elif username != '123456' and password != '123456':
        return '账号或密码错误', 201
    else:
        return render_template('')


if __name__ == '__main__':
    app.debug = True
    app.run(host='172.10.25.26', port='80', debug=True)
