class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        return customer.age >= 18

    def check_drunkenness(self, customer):
        return customer.drunkenness > 5
