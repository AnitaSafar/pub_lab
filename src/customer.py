class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def reduce_wallet(self, cost):
        self.wallet -= cost