class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        if customer.age >= 18:
            return "Old enough"
        return "Too young"

    def check_drunkenness(self, customer):
        if customer.drunkenness > 5:
            return "Refuse!!"
        return "Serve.."

    def buy_drink(self, drink, customer):
        if self.check_age(customer) == "Old enough" and self.check_drunkenness(customer) == "Serve..":
            customer.wallet -= drink.price
            self.till += drink.price
            customer.drunkenness += drink.alcohol_level
        return "Leave pub!"