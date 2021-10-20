import unittest
from src.drinks import Drinks

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("beer", 3, 1)

    def test_drink_has_name(self):
        self.assertEqual("beer", self.drinks.name)

    def test_drink_has_price(self):
        self.assertEqual(3, self.drinks.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(1, self.drinks.alcohol_level)