#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask_apscheduler import APScheduler

from common import ConfigUtil

config = ConfigUtil.ConfigUtil('application.properties')
rocketConf = config.getDict('rocket')
from AppInit import app
from control.schedul.agentTimer import *
from RegisterBlueViews import *

if __name__ == '__main__':
    # scheduler = APScheduler()
    # scheduler.init_app(app)
    # scheduler.start()
    host = rocketConf.get('rocket.host', '0.0.0.0')
    port = rocketConf.get('rocket.port', '80')
    app.run(host, port)
