class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def reduce_wallet(self, cost):
        self.wallet -= cost

    def buy_drink(self, drink, pub):
        self.wallet -= drink.price
        pub.till += drink.price