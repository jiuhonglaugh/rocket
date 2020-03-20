#!/usr/bin/env python
# -*- coding:utf-8 -*-

import RegisterBlueViews
from common import ConfigUtil
from control.views import errorPage

config = ConfigUtil.ConfigUtil('application.properties').getDict('rocket')
from AppInit import app

if __name__ == '__main__':
    host = config.get('rocket.host', '0.0.0.0')
    port = config.get('rocket.port', '80')
    app.run(host, port)
