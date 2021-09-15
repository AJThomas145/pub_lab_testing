class Customer:

    def __init__(self, input_name, input_wallet):
        self.name = input_name
        self.wallet = input_wallet
        self.drinks = []
        
    def pay_for_drink(self, price_of_drink):
        self.wallet -= price_of_drink

    def customer_takes_drink(self, drink):
        self.drinks.append(drink)

    def number_of_drinks(self):
        return len(self.drinks)