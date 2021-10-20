import unittest
from src.customer import Customer
from src.drinks import Drinks
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", 20, 18)

    def test_customer_has_name(self):
        self.assertEqual("John", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3)
        self.assertEqual(17, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(18, self.customer.age)

    

    