# https://github.com/saco-03/lab10-IO-JY
# Partner 1: Isaac Osorio
# Partner 2: Jerry Yao
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(-6, 4), -2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(-6, 4), -10)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5, 10), 50)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(5, -10), -50)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 50), 5)
        self.assertEqual(div(-5, 10), -2)
        self.assertAlmostEqual(div(7, 3), 2.3333333)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(3, 9), 2)
        self.assertEqual(logarithm(16, 2), 0.25)
        self.assertEqual(logarithm(5, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 2)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(5, -12), 13.0)
        self.assertAlmostEqual(hypotenuse(2, 3), 3.6055513)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
           square_root(-4)
        self.assertEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(8), 2.8284271)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()