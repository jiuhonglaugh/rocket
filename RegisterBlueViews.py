#!/usr/bin/env python
# -*- coding:utf-8 -*-
from control.views.loginBlue import login_blue
from control.views.hostBlue import hostInfo_blue
from control.views.sshBlue import ssh_blue
from control.views.fileBlue import file_blue
from control.views.agentBlue import agent_blue
from control.views.lightBlue import light_blue
from control.views import errorPage
from main import app

app.register_blueprint(login_blue, ull_prefix='/')
app.register_blueprint(hostInfo_blue, ull_prefix='/host')
app.register_blueprint(ssh_blue, ull_prefix='/ssh')
app.register_blueprint(file_blue, ull_prefix='/file')
app.register_blueprint(agent_blue, ull_prefix='/agent')
app.register_blueprint(light_blue, ull_prefix='/light')
