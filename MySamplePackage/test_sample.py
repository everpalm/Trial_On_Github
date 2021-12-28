# content of test_sample.py

import logging
import pytest

from MySamplePackage.sample import MySample

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TestSample():
    #@pytest.fixture(scope="function", autouse=True)
    def test_set_func(self):
        QOO = MySample(1)
        #logging.DEBUG("QOO.set_func() = %x", QOO.set_func())
        #MyX = QOO.set_func()
        #print(f'QOO = {MyX}')
        #print(f'QOO = {QOO.set_func()}')
        logger.debug('QOO.set_func = %x', QOO.set_func())
        #logger.debug('test')
        assert QOO.set_func() == 2
        
    def test_tomato_func(self):
        QOO = MySample(2)
        #logger.debug('QOO.tomato = %x', QOO.tomato_func())
    

