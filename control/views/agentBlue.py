#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from control.manager.agentManager import getAgentHostDetail
from common.Logger import Logger

agent_blue = Blueprint('agent', __name__)
log = Logger(loggername='agent_blue')

@agent_blue.route('/agent/base')
def base():
    result = getAgentHostDetail()
    return result
