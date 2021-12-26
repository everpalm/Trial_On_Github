import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

#print('hello world')
logging.info('sample.py')
    
class MySample():
    def __init__(self, int_x):
        self.int_x = int_x
    
    def get_int_x(self):
        return self.int_x
        
    def set_func(self):
        logger.debug('self.int_x = %x', self.get_int_x())
        return self.int_x + 1

    def tomato_func(self):
        #logger.debug('tell me about that...')
        return self.init_x
