import unittest

from shop import add, remove, show, checkout


class TestShop(unittest.TestCase):
    def setUp(self):
        self.basket = {}

    def test_shop_adds_item_to_basket(self):
        add(self.basket, "pizza", 4)
        self.assertEqual(self.basket["pizza"], 4)

    def test_shop_adding_same_item_increments(self):
        add(self.basket, "pizza", 4)
        add(self.basket, "pizza", 1)
        self.assertEqual(self.basket["pizza"], 5)

    def test_shop_add_throws_exception_item_not_found(self):
        self.assertRaises(ValueError, add, self.basket, "garlic bread", 2)

    def test_shop_remove_reduces_item_quant_in_basket(self):
        self.basket["pizza"] = 4
        remove(self.basket, "pizza", 1)
        self.assertEqual(self.basket["pizza"], 3)

    def test_shop_remove_removes_item_from_basket(self):
        self.basket["pizza"] = 4
        remove(self.basket, "pizza", 4)
        self.assertEqual("pizza" in self.basket.keys(), False)

    def test_shop_remove_throws_exception_item_not_found(self):
        self.assertRaises(ValueError, remove, self.basket, "garlic bread", 2)

    def test_show_has_readable_output(self):
        self.basket["pizza"] = 2
        self.basket["lemonade"] = 2
        self.assertEqual(
            show(self.basket), "Your basket:\n\npizza x2 (£21.0)\nlemonade x2 (£5.0)\n"
        )

    def test_checkout_shows_total_price(self):
        self.basket["pizza"] = 2
        self.basket["lemonade"] = 2
        self.assertEqual(checkout(self.basket), "Your total is: £26.0")


if __name__ == "__main__":
    unittest.main()
