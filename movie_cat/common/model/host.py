from sqlalchemy import Integer,String

from application import db

class Ops_host(db.Model):
    __tablename__ = 'ops_host'

    id = db.Column(Integer, primary_key=True)
    host_name = db.Column(String(255))
    host_ip = db.Column(String(255))
    host_total_disk = db.Column(String(255))
    host_root_remain_disk = db.Column(String(255))
    host_total_memory = db.Column(String(255))
    host_free_memory = db.Column(String(255))
    host_used_memory = db.Column(String(255))
    host_total_cpu = db.Column(Integer)
    host_necard_kind = db.Column(String(255))
