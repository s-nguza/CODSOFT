# mytests.py
import unittest
import logic_Cal as calc

class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(6, 3), 2)
        with self.assertRaises(ValueError):
            calc.divide(6, 0)

if __name__ == '__main__':
    unittest.main()
