from common import timeUtil
from common.dbUtil import getDBURI
class Config:
    SECRET_KEY = 'hard to guess string'
    '''
    1.数据库地址，用户，密码，数据库名称
    2.动态跟踪修改如果设置为True会影响执行效率
    3.自动提交
    4.数据库连接回收时间
    5.数据库连接池大小
    6.打印执行的sql脚本
    7.session过期时间
    8.是否打卡idebug 模式
    '''
    SQLALCHEMY_DATABASE_URI = getDBURI()
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_POOL_RECYCLE = 10
    SQLALCHEMY_POOL_SIZE = 30
    SQLALCHEMY_ECHO = False
    PERMANENT_SESSION_LIFETIME = timeUtil.sessionTimeOut(minutes=15)
    DEBUG = True
    # DEBUG = False
    JOBS = [
        {
            'id': 'agentTask', # 任务id
            'func': '__main__:agentTask', # 任务执行程序
            'args': None, # 执行程序参数
            'trigger': 'interval', # 任务执行类型，定时器
            'seconds': 20, # 任务执行时间，单位秒
        }
    ]
