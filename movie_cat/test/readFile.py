import configparser
import os
from movie_cat.common.utils.fileUtils import FileUtils

print(FileUtils.getConfigFilePath('application.properties'))

print('==========================================')
#获取当前目录上一级目录,
#abspath获取的是'文件'的绝对路径
#目录也可以看成文件，目录上一层就是他的文件夹，用dirname获取文件夹名称
# path = os.path.dirname(os.path.abspath('.'))
# print(path)
#
# print("#os.path.abspath('.')")
# path = os.path.abspath('.')
# print(path)
path = os.path.dirname(os.path.abspath('.'))
print('os.path.abspath========'+os.path.abspath('.'))
print(path)
print("###os.path.dirname")
print('1============='+os.path.dirname(path))
path = os.path.dirname(path)
print('2============='+os.path.dirname(path))


path = os.getcwd()
print(path)

cf = configparser.RawConfigParser()
cf.read(r'D:\JetBrainsPyCharm2019\pyNameSpace\py\test\movie_cat\config\application.properties')
#返回的是一个list
secs = cf.sections()
print(secs)

#返回一个list,为某个section下面全部得key
options = cf.options(secs[0])
print(options)

#返回某个section下面全部得键值对key:value
items = cf.items(secs[0])
print(items)

#返回某个具体的配置项值
logs_clevel = cf.get(secs[0],'logs.clevel')
print(logs_clevel)

items = cf.items('logger')[0][0]
print(items)

