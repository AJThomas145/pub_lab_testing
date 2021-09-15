class Pub:

    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.drinks_list = []

    def number_of_drinks(self):
        return len(self.drinks_list)

    def add_cash_to_till(self, price_of_drink):
        self.till += price_of_drink