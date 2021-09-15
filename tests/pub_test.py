import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("beer", 5.00)
        self.customer = Customer("Simon", 30.00, 16)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.till)

    # @unittest.skip("delete this line to run the test")
    def test_pub_has_drinks(self):
        self.assertEqual(0, self.pub.number_of_drinks())

    # @unittest.skip("delete this line to run the test")
    def test_add_cash_to_till(self):
        self.pub.add_cash_to_till(5.00)
        self.assertEqual(105.00, self.pub.till)

    # @unittest.skip("delete this line to run the test")
    def test_add_drink_from_list(self):
        self.pub.add_drink_to_list(self.drink)
        self.assertEqual(1, self.pub.number_of_drinks())

    # @unittest.skip("delete this line to run the test")
    def test_remove_drink_from_list(self):
        self.pub.add_drink_to_list(self.drink)
        self.pub.remove_drink_from_list(self.drink)
        self.assertEqual(0, self.pub.number_of_drinks())

    def test_is_customer_old_enough(self):
        self.assertEqual(False, self.pub.customer_is_old_enough(self.customer))  

    # @unittest.skip("delete this line to run the test")
    def test_customer_buys_drink_from_pub(self):
        self.pub.add_drink_to_list(self.drink)
        self.pub.sell_drink_to_customer(self.customer, self.drink)
        self.assertEqual(25, self.customer.wallet)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(0, self.pub.number_of_drinks())
        