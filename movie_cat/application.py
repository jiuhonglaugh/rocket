# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask( __name__ )
#核心对象初始化

#manager = Manager( app )

#app.config.from_pyfile( "config/base_setting.py" )
#ops_config=local|production
#linux export ops_config=local|production
#windows set ops_config=local|production
#if "ops_config" in os.environ:
#    app.config.from_pyfile( "config/%s_setting.py"%( os.environ['ops_config'] ) )
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://flask:123456@172.10.4.100/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy( app )


