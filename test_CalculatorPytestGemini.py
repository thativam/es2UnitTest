import unittest
import math
from Calculator import Calculator
class CalculatorTestGemini(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Basic Arithmetic Tests
    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-2, 7), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        # Test with floats
        self.assertAlmostEqual(self.calc.add(3.14, 1.59), 4.73, places=2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(3, -2), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Test with floats
        self.assertAlmostEqual(self.calc.subtract(5.2, 1.8), 3.4, places=2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-5, 2), -10)
        self.assertEqual(self.calc.multiply(1, 0), 0)
        # Test with floats
        self.assertAlmostEqual(self.calc.multiply(4.5, 2.0), 9.0, places=2)

    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 3), 4)
        self.assertEqual(self.calc.divide(-8, 2), -4)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 10, 0)
        # Test with floats
        self.assertAlmostEqual(self.calc.divide(10.5, 2.0), 5.25, places=2)

    # Factorial Tests
    def test_factorial(self):
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertRaises(TypeError, self.calc.factorial, -3)

    # Trigonometric Tests (using math.radians and math.degrees for consistency)
    def test_sin(self):
        # Test with radians
        self.assertAlmostEqual(self.calc.sin(math.radians(30)), 0.5, places=2)
        self.assertAlmostEqual(self.calc.sin(math.radians(90)), 1.0, places=2)
        # Test with degrees (using degreesToRadians)
        self.assertAlmostEqual(self.calc.sin(self.calc.degreesToRadians(45)), 0.707, places=2)

    def test_cos(self):
        # Test with radians
        self.assertAlmostEqual(self.calc.cos(math.radians(0)), 1.0, places=2)
        self.assertAlmostEqual(self.calc.cos(math.radians(180)), -1.0, places=2)
        # Test with degrees (using degreesToRadians)
        self.assertAlmostEqual(self.calc.cos(self.calc.degreesToRadians(60)), 0.5, places=2)

    def test_tan(self):
        # Test with radians (consider edge cases like pi/2)
        self.assertAlmostEqual(self.calc.tan(math.radians(45)), 1.0, places=2)
        self.assertRaises(ZeroDivisionError, self.calc.tan, math.radians(90))
        # Test with degrees (using degreesToRadians)
        self.assertAlmostEqual(self.calc.tan(self.calc.degreesToRadians(30)), math.tan(math.radians(30)), places=2)  # Avoid redundant calculation

    # Other Mathematical Functions
    def test_exp(self):
        self.assertEqual(self.calc.exp(2, 3), 8)
        self.assertEqual(self.calc.exp(1, 0), 1)
