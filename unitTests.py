import unittest
from ConfParser import *

class ConfTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.config = YakeiConfig()

    def test_listDomains(self):
        self.assertEqual(len(self.config.GetDomains()),2)
        
    def test_listServicesFailure(self):
        with self.assertRaises(DomainNotFound):
            self.config.GetServices("abc")
            
    def test_listServicesPass(self):
        self.assertEqual(len(self.config.GetServices("git.vertinext.com")),1)