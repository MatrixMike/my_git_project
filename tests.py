#tests.py
import unittest
from sum import add_two_numbers


class TestsForAddFunction(unittest.TestCase):

    def test_zeros(self):
        result = add_two_numbers(0, 0)
        self.assertEqual(0, result)

    def test_both_positive(self):
        result = add_two_numbers(5, 7)
        self.assertEqual(12, result)

    def test_both_negative(self):
        result = add_two_numbers(-5, -7)
        self.assertEqual(-12, result)

    def test_one_negative(self):
        result = add_two_numbers(5, -7)
        self.assertEqual(-2, result)

if __name__ == '__main__':
    unittest.main()
