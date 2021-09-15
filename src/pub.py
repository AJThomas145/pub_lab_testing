class Pub:

    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.drinks_list = []

    def number_of_drinks(self):
        return len(self.drinks_list)

    def add_cash_to_till(self, price_of_drink):
        self.till += price_of_drink

    def add_drink_to_list(self, drink):
        self.drinks_list.append(drink)

    def remove_drink_from_list(self, drink):
        self.drinks_list.remove(drink)

    def customer_is_old_enough(self, customer):
        if customer.age >= 18:
            return True

        return False

    def sell_drink_to_customer(self, customer, drink):
        customer.pay_for_drink(drink.price)
        self.add_cash_to_till(drink.price)
        self.remove_drink_from_list(drink)
        
