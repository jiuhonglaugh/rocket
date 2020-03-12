from werkzeug.security import generate_password_hash, check_password_hash
from main import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String(300))

    def __init__(self, name, password):
        self.name = name
        self.password = password

    @staticmethod
    def query_by_username(name):
        return User.query.filter(User.name == name).first()

    @property
    def pwd(self):
        raise AttributeError(u'密码不可读')

    @pwd.setter
    def pwd(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        if self.password == password:
            return True
        else:
            return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User:%s>' % self.name
