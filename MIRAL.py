# qa_activity

import unittest

def sum(n1, n2):
    return n1 + n2

class SumTestCase(unittest.TestCase):
    def test_positive_numbers(self):
        result = sum(3, 5)
        self.assertEqual(result, 8)

    def test_negative_numbers(self):
        result = sum(-2, -7)
        self.assertEqual(result, -9)

    def test_zero_and_positive_number(self):
        result = sum(0, 9)
        self.assertEqual(result, 9)

    def test_zero_and_negative_number(self):
        result = sum(0, -4)
        self.assertEqual(result, -4)

    def test_zero_and_zero(self):
        result = sum(0, 0)
        self.assertEqual(result, 0)

# Run the unit test
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
