import unittest
from eligibility import shipping_cost, validate_request


class AppTests(unittest.TestCase):
    def test_shipping_under(self):
        self.assertEqual(shipping_cost(40), 7)

    def test_shipping_over(self):
        self.assertEqual(shipping_cost(60), 0)

    def test_shipping_exact_boundary(self):
        self.assertEqual(shipping_cost(50), 7)

    def test_negative_age_rejected(self):
        with self.assertRaises(ValueError):
            validate_request(-1, 2)

    def test_valid_party(self):
        validate_request(30, 2)


if __name__ == '__main__':
    unittest.main()
