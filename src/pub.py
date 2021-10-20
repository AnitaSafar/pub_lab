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
