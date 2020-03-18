import datetime
import json


def toDict(inst, cls):
    d = dict()
    '''
    获取表里面的列并存到字典里面
    '''
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        d[c.name] = v
    return d


def toJson(inst, cls):
    dt = toDict(inst, cls)
    return json.dumps(dt, cls=DateEncoder)


def toJsonAll(result):
    jsonList = list()
    dtList = toDictAll(result)
    for dt in dtList:
        jsonList.append(json.dumps(dt, cls=DateEncoder))
    return jsonList


def toDictAll(result):
    dtList = list()
    for item in result:
        dt = dict()
        for key in item.keys():
            dt[key] = getattr(item, key)
        dtList.append(dt)
    return dtList


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
