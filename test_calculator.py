#https://github.com/Ironarjun/lab11-AS-IM.git
#Arjun Suresh
#Luliana Mashchenko
import unittest
from calculator import add, sub, mul, div, exp, log, square_root, hypotenuse
import math

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)
        self.assertIsNone(square_root(-4))  # should handle negative numbers safely

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertIsNone(hypotenuse("a", 4))  # invalid type

    def test_add(self):
        self.assertEqual(add(3, 5), 8)

    def test_sub(self):
        self.assertEqual(sub(10, 4), 6)

    def test_mul(self):
        self.assertEqual(mul(3, 4), 12)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_log(self):
        self.assertAlmostEqual(log(8, 2), 3)
        with self.assertRaises(ValueError):
            log(-1, 2)
        with self.assertRaises(ValueError):
            log(8, 1)

    def test_exp(self):
        self.assertEqual(exp(2, 3), 8)

if __name__ == '__main__':
    unittest.main()


if __name__ == "__main__":
    unittest.main()