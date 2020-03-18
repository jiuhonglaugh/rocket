import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info('start print log')
logger.debug('test debug log')
logger.warning('test warning log')
logger.info('end print log')