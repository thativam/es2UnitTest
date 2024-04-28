import pytest
from Calculator import Calculator
import math

class TestCalculatorCopilot:
    @pytest.fixture(scope="class")
    def calc(self):
        return Calculator()

    def test_add(self, calc):
        assert calc.add(1, 2) == 3
        assert calc.add(-1, 1) == 0
        assert calc.add(-1, -1) == -2

    def test_subtract(self, calc):
        assert calc.subtract(10, 5) == 5
        assert calc.subtract(-1, -1) == 0
        assert calc.subtract(-1, 1) == -2

    def test_multiply(self, calc):
        assert calc.multiply(3, 5) == 15
        assert calc.multiply(-1, 3) == -3
        assert calc.multiply(0, 10) == 0

    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5
        assert calc.divide(-1, 1) == -1
        with pytest.raises(ZeroDivisionError):
            calc.divide(1, 0)

    def test_factorial(self, calc):
        assert calc.factorial(5) == 120
        assert calc.factorial(0) == 1
        with pytest.raises(TypeError):
            calc.factorial(-1)

    def test_sin(self, calc):
        assert calc.sin(math.pi/2) == 1
        assert calc.sin(0) == 0
        assert abs(calc.sin(math.pi) - 0) < 0.0001

    def test_cos(self, calc):
        assert calc.cos(math.pi/2) == pytest.approx(0, abs=1e-9)
        assert calc.cos(0) == 1
        assert abs(calc.cos(math.pi) + 1) < 0.0001

    def test_tan(self, calc):
        assert abs(calc.tan(0) - 0) < 0.0001
        assert abs(calc.tan(math.pi/4) - 1) < 0.0001

    def test_degrees_to_radians(self, calc):
        assert calc.degreesToRadians(180) == math.pi
        assert calc.degreesToRadians(360) == 2 * math.pi

    def test_negative_add(self, calc):
        assert calc.add(-5, -10) == -15
        assert calc.add(-2, 5) == 3

    def test_negative_subtract(self, calc):
        assert calc.subtract(-10, -5) == -5
        assert calc.subtract(5, -2) == 7

    def test_negative_multiply(self, calc):
        assert calc.multiply(-3, -5) == 15
        assert calc.multiply(-2, 5) == -10

    def test_negative_divide(self, calc):
        assert calc.divide(-10, 2) == -5
        assert calc.divide(1, -1) == -1

    def test_large_factorial(self, calc):
        assert calc.factorial(10) == 3628800
        assert calc.factorial(20) == 2432902008176640000

    def test_large_sin(self, calc):
        assert abs(calc.sin(math.pi/3) - 0.86602540378) < 0.0001
        assert abs(calc.sin(math.pi/6) - 0.5) < 0.0001

    def test_large_cos(self, calc):
        assert abs(calc.cos(math.pi/3) - 0.5) < 0.0001
        assert abs(calc.cos(math.pi/6) - 0.86602540378) < 0.0001

    def test_large_tan(self, calc):
        assert abs(calc.tan(math.pi/3) - 1.73205080757) < 0.0001
        assert abs(calc.tan(math.pi/6) - 0.57735026919) < 0.0001

    def test_large_degrees_to_radians(self, calc):
        assert calc.degreesToRadians(90) == math.pi/2
        assert calc.degreesToRadians(270) == 3 * math.pi/2