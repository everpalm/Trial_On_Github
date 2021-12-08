import pytest
import logging
from test_sample import func 

logging.basicConfig(filename='example.log', level=logging.DEBUG)

#print('hello world')
logging.warning('test!')
logging.info('what the hell?')
    
def test_func():
    assert func(3) == 4
    
