class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def reduce_wallet(self, cost):
        self.wallet -= cost

    def buy_drink(self, drink, pub):
        self.wallet -= drink.price
        pub.till += drink.price
        self.drunkenness += drink.alcohol_level