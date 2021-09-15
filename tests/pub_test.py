import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(3, self.pub.drinks_list())

    def test_add_cash_to_till(self):
        self.assertEqual(110.00, self.pub.add_cash_to_till(price_of_drink))

    def test_remove_drink_from_list(self):
        self.pub.remove_drink_from_list(drink_sold)
        self.assertEqual(2, self.pub.pub.drinks_list())