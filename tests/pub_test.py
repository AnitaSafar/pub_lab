import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        stock = {
            "drink": {
                "beer": 50,
                "wine": 30
            },
            "food": {
                "chips": 20,
                "burgers": 15
            },
            }
        self.pub = Pub("The Chanter", 300, [], stock)


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
        new_customer = Customer("Alfred", 10, 17)
        pub_check = self.pub.check_age(new_customer)
        self.assertEqual("Too young", pub_check)

    def test_check_drunkenness(self):
        new_customer = Customer("Alfred", 10, 17)
        new_customer.drunkenness = 6
        drunk_check = self.pub.check_drunkenness(new_customer)
        self.assertEqual("Refuse!!", drunk_check)

    def test_check_drunkenness_false(self):
        new_customer = Customer("Alfred", 10, 17)
        drunk_check = self.pub.check_drunkenness(new_customer)
        self.assertEqual("Serve..", drunk_check)

    def test_buy_drink(self):
        new_drink = Drinks("beer", 3, 1)
        new_customer = Customer("John", 20, 18)
        self.pub.buy_drink(new_drink, new_customer)
        self.assertEqual(17, new_customer.wallet)

    def test_buy_drink_changes_till(self):
        new_drink = Drinks("beer", 3, 1)
        new_customer = Customer("John", 20, 18)
        self.pub.buy_drink(new_drink, new_customer)
        self.assertEqual(303, self.pub.till)

    def test_buy_drink_changes_drunkenness(self):
        new_drink = Drinks("beer", 3, 1)
        new_customer = Customer("John", 20, 18)
        self.pub.buy_drink(new_drink, new_customer)
        self.assertEqual(1, new_customer.drunkenness)

    def test_buy_drink_young_and_drunk(self):
        new_drink = Drinks("beer", 3, 1)
        new_customer = Customer("John", 20, 17)
        new_customer.drunkenness = 6
        result = self.pub.buy_drink(new_drink, new_customer)
        self.assertEqual("Leave pub!", result)

    def test_buy_food(self):
        new_food = Food("chips", 2, 1)
        new_customer = Customer("John", 20, 18)
        new_customer.drunkenness = 1
        self.pub.buy_food(new_food, new_customer)
        self.assertEqual(0, new_customer.drunkenness)

    def test_buy_food_two(self):
        new_food = Food("burger", 5, 2)
        new_customer = Customer("John", 20, 18)
        new_customer.drunkenness = 1
        self.pub.buy_food(new_food, new_customer)
        self.assertEqual(0, new_customer.drunkenness)

    def test_pub_has_stock(self):
        stock = {
            "drink": {
                "beer": 50,
                "wine": 30
            },
            "food": {
                "chips": 20,
                "burgers": 15
            },
        }
        self.assertEqual(stock, self.pub.stock)

    def test_pub