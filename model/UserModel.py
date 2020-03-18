from werkzeug.security import generate_password_hash, check_password_hash
from main import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'ops_user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, index=True)
    user_pwd = db.Column(db.String(300))

    def __init__(self, user_name, user_pwd):
        self.user_name = user_name
        self.user_pwd = user_pwd

    @staticmethod
    def query_by_username(user_name):
        return User.query.filter(User.name == user_name).first()

    @property
    def pwd(self):
        raise AttributeError(u'密码不可读')

    @pwd.setter
    def pwd(self, user_pwd):
        self.user_pwd = generate_password_hash(user_pwd)

    def verify_password(self, user_pwd):
        if self.user_pwd == user_pwd:
            return True
        else:
            return check_password_hash(self.user_pwd, user_pwd)

    def __repr__(self):
        return '<User:%s>' % self.user_name
