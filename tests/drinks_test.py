import unittest
from src.drinks import Drinks

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("beer", 3)

    def test_drink_has_name(self):
        self.assertEqual("beer", self.drinks.name)

    def test_drink_has_price(self):
        self.assertEqual(3, self.drinks.price)