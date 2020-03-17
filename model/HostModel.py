from werkzeug.security import generate_password_hash, check_password_hash
from main import db
from flask_login import UserMixin


class HostInfoModel(db.Model, UserMixin):
    __tablename__ = 'ops_host'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    host_name = db.Column(db.String(255), unique=True, index=True)
    host_ip = db.Column(db.String(255))
    host_total_disk = db.Column(db.Integer)
    host_root_remain_disk = db.Column(db.Integer)
    host_total_memory = db.Column(db.Integer)
    host_free_memory = db.Column(db.Integer)
    host_used_memory = db.Column(db.Integer)
    host_total_cpu = db.Column(db.Integer)
    host_necard_kind = db.Column(db.String(255))
    status = db.Column(db.String(255))
    update_time = db.Column(db.String(255))

    def __init__(self, host_name, host_ip, host_total_disk, host_root_remain_disk, host_total_memory, host_free_memory,
                 host_used_memory, host_total_cpu, host_necard_kind):
        self.host_name = host_name
        self.host_ip = host_ip
        self.host_total_disk = host_total_disk
        self.host_root_remain_disk = host_root_remain_disk
        self.host_total_memory = host_total_memory
        self.host_free_memory = host_free_memory
        self.host_used_memory = host_used_memory
        self.host_total_cpu = host_total_cpu
        self.host_necard_kind = host_necard_kind

    def setStatus(self, status):
        self.status = status

    @staticmethod
    def query_by_hostsName(id):
        return HostInfoModel.query.filter(HostInfoModel.id == id).first()

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

    @staticmethod
    def all():
        return HostInfoModel.query.all()

    @staticmethod
    def with_entities(*entities):
        return HostInfoModel.query.with_entities(*entities)

    def __repr__(self):
        return '<HostInfo:%s>' % self.id
