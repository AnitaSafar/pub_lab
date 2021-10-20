import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Chanter", 300, [])

    def test_pub_has_name(self):
        self.assertEqual("The Chanter", self.pub.name)