import logging
# logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logger.info('start print log')
# logger.debug('test debug log')
# logger.warning('test warning log')
# logger.info('end print log')
"""
获取logger对象
"""
logger = logging.getLogger(__name__)
#设置日志格式
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.setLevel(level=logging.INFO)
#设置文件日志
hander = logging.FileHandler(r'D:\JetBrainsPyCharm2019\pyNameSpace\py\test\movie_cat\common\logs/test.log')
hander.setLevel(logging.INFO)
hander.setFormatter(format)
logger.addHandler(hander)
#设置控制台日志
console = logging.StreamHandler()
console.setFormatter(format)
console.setLevel(logging.INFO)
logger.addHandler(console)

logger.info('start print log')
logger.debug('test debug log')
logger.warning('test warning log')
logger.info('end print log')
