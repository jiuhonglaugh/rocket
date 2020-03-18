#!/usr/bin/env python
# -*- coding:utf-8 -*-
from control.views.loginBlue import login_blue
from control.views.hostBlue import hostInfo_blue
from control.views.manager import manager_blue
from main import app

app.register_blueprint(login_blue, ull_prefix='/')
app.register_blueprint(hostInfo_blue, ull_prefix='/host')
app.register_blueprint(manager_blue, ull_prefix='/host')
