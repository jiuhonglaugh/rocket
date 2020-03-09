from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from flask import  render_template
import config


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


@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost',port='80',debug=True)