from Calculator import Calculator
import unittest
import math

class TesteClass(unittest.TestCase):
    def testeSoma(self):
        Calc  = Calculator()
        self.assertEqual(23, Calc.add(15,8), "Soma esta errada")
    def testeSub(self):
        Calc  = Calculator()
        self.assertEqual(23, Calc.subtract(31,8), "Subtração esta errada")
    def testeMult(self):
        Calc  = Calculator()
        self.assertEqual(24, Calc.multiply(4,6), "Multiplicação esta errada")
    def testeDiv(self):
        Calc  = Calculator()
        self.assertEqual(4, Calc.divide(36,9), "Divisão esta errada")
    def testeFactorial(self):
        Calc  = Calculator()
        self.assertEqual(39916800, Calc.factorial(11), "Fatorial esta errada")
    def testeSin(self):
        Calc  = Calculator()
        self.assertEqual(0.49999999999999994, Calc.sin(0.5235987755982988), "Calc esta errada")
    def testeCos(self):
        Calc  = Calculator()
        self.assertEqual(0.5000000000000001, Calc.cos(1.0471975511965976), "Calc esta errada")
    def testeTan(self):
        Calc  = Calculator()
        self.assertEqual(1, Calc.tan(0.7853981633974483), "Calc esta errada")
    def testeRad(self):
        Calc  = Calculator()
        self.assertEqual(0.5235987755982988, Calc.degreesToRadians(30), "Calc esta errada")
    

if __name__ == "__main__":
    unittest.main()