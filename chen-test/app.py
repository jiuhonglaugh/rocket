from flask import Flask

#应用入口
app = Flask(__name__)

#url对应视图
@app.route('/index')
def index():
    return '<h1>hello world</h1>'

if __name__ == '__main__':
    app.run()

