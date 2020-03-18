#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect

from conf import AppConfig

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(AppConfig.Config)
csrf = CsrfProtect()
csrf.init_app(app)
db.init_app(app)
