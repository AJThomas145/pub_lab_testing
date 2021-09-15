import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Simon", 30.00, 16)
        self.drink = Drink("beer", 5.00)

    def test_does_customer_have_name(self):
        self.assertEqual("Simon", self.customer.name)

    def test_does_customer_have_money(self):
        self.assertEqual(30.00, self.customer.wallet)

    def test_customer_pays(self):
        self.customer.pay_for_drink(self.drink.price)
        self.assertEqual(25, self.customer.wallet)

    # @unittest.skip("delete this line to run the test")
    def test_give_customer_drink(self):
        self.customer.customer_takes_drink(self.drink)
        self.assertEqual(1, self.customer.number_of_drinks())

    def test_customer_number_of_drinks(self):
        self.assertEqual(0, self.customer.number_of_drinks())

    