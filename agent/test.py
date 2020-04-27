from threading import Thread
from time import sleep


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


@async
def A():
    sleep(1)
    print("函数A睡了十秒钟。。。。。。")
    print("a function")

def B():
    print("b function")


if __name__ == '__main__':
    url = "curl -u elastic:infobeat123 http://node2:9200/_cat/nodes -XGET"
    print(url)