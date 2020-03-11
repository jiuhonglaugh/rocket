from flask import  Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import  render_template
from flask import  request,jsonify
from flask import url_for
import config
import testsql

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'hard to guess string'


class SysMonitInfo(db.Model):
    """采集Linux系统的数据"""
    __tablename__ = 'sysmonitinfo'

    id = db.Column(db.Integer, primary_key=True)
    cpu1mload = db.Column(db.String(10))
    cpu5mload = db.Column(db.String(10))
    meminfo = db.Column(db.String(10))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/viewdata',methods=['post'])
def viewdata():
    if request.method == 'post':
        res = testsql.selectByParameters('select cpu1mload,cpu5mload,meminfo from sysmonitinfo;')
        return jsonify(sys_cpu1mload = [x[0] for x in res],
                       sys_cpu5mload = [x[1] for x in res],
                       mem_info =[x[2] for x in res])


if __name__ == '__main__':
    app.run(host='localhost',port='80',debug=True)