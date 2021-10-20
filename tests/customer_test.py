import unittest
from src.customer import Customer
from src.drinks import Drinks
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", 20)

    def test_customer_has_name(self):
        self.assertEqual("John", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3)
        self.assertEqual(17, self.customer.wallet)

    def test_buy_drink(self):
        new_drink = Drinks("beer", 3)
        new_pub = Pub("The Chanter", 300, [])
        self.customer.buy_drink(new_drink, new_pub)
        self.assertEqual(17, self.customer.wallet)

    def test_buy_drink_changes_till(self):
        new_drink = Drinks("beer", 3)
        new_pub = Pub("The Chanter", 300, [])
        self.customer.buy_drink(new_drink, new_pub)
        self.assertEqual(303, new_pub.till)