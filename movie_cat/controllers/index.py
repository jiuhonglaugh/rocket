from flask import Blueprint,render_template
from sqlalchemy import text
from application import db
from common.model.user import Ops_user

#申明一个蓝图对象
index_page = Blueprint('index_page',__name__)

@index_page.route('/')
def index():
    dict = {'name':'b'}
    #sql = text('select user from `user`;')
    #result = db.engine.execute(sql)
    #查询
    result = Ops_user.query.all()


    #实例化一个对象，并插入数据库
    # userModel = Ops_user()
    # userModel.user_name = 'system'
    # userModel.user_pwd = 'system'
    # db.session.add(userModel)
    # db.session.commit()

    #
    query = Ops_user.query.filter(Ops_user.id == 2) #.first()只返回一个
    dict['query'] = query

    query1 = Ops_user.query.first()
    dict['query1'] = query1

    print(result)
    dict['mysql_user'] = result
    dict['user'] = {'name':'zsq','age':2666666663,'addr':'安徽省'}
    dict['number_list'] = [1,2,3,4,5]
    #可以传递一个字典（可以是元组，可以是字典）
    return render_template('index2.html',**dict)

@index_page.route('/login')
def login():
    return render_template('login.html')

@index_page.route('/head')
def head():
    return 'pass'



