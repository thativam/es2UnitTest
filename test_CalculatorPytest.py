import pytest
from Calculator import Calculator
import math

class TestCalculatorChatgpt4:
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
        assert calc.cos(math.pi/2) == 0
        assert calc.cos(0) == 1
        assert abs(calc.cos(math.pi) + 1) < 0.0001

    def test_tan(self, calc):
        assert abs(calc.tan(0) - 0) < 0.0001
        assert abs(calc.tan(math.pi/4) - 1) < 0.0001

    def test_degrees_to_radians(self, calc):
        assert calc.degrees_to_radians(180) == math.pi
        assert calc.degrees_to_radians(360) == 2 * math.pi