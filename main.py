#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from utils.dbUtil import getDBURI


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




if __name__ == '__main__':
    app.run(host='172.10.25.26', port='80', debug=True)
