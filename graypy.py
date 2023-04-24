import logging
import graypy
#graypy python module for logger data to graylog

my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFUDPHandler('localhost', 12201)
my_logger.addHandler(handler)

my_logger.debug('Hello Graylog campaign.')