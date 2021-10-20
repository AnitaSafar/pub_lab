import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Chanter", 300, [])

    def test_pub_has_name(self):
        self.assertEqual("The Chanter", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(300, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual([], self.pub.drinks)

    def test_increase_till(self):
        self.pub.increase_till(3)
        self.assertEqual(303, self.pub.till)

    def test_check_age_true(self):
        new_customer = Customer("John", 20, 18)
        pub_check = self.pub.check_age(new_customer)
        self.assertEqual("Old enough", pub_check)

    def test_check_age_false(self):
        new_customer = Customer("John", 20, 17)
        pub_check = self.pub.check_age(new_customer)
        self.assertEqual("Too young", pub_check)

    def test_check_drunkenness(self):
        new_customer = Customer("John", 20, 17)
        new_customer.drunkenness = 6
        drunk_check = self.pub.check_drunkenness(new_customer)
        self.assertEqual("Refuse!!", drunk_check)

    def test_check_drunkenness_false(self):
        new_customer = Customer("John", 20, 17)
        drunk_check = self.pub.check_drunkenness(new_customer)
        self.assertEqual("Serve..", drunk_check)
