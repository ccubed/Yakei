import unittest
from ConfParser import *

class ConfTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.config = YakeiConfig()

    def test_listDomains(self):
        self.config.GetDomains()
        
    def test_listServices(self):
        self.config.GetServices("abc")