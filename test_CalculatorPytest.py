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
        self.assertEqual(0.49999999999999994, Calc.sin(math.pi/6), "Seno esta errado")
    def testeCos(self):
        Calc  = Calculator()
        self.assertEqual(0.5000000000000001, Calc.cos(math.pi/3), "Cosseno esta errado")
    def testeTan(self):
        Calc  = Calculator()
        self.assertEqual(1, Calc.tan(math.pi/4), "Tangente esta errada")
    def testeRad(self):
        Calc  = Calculator()
        self.assertEqual(0.5235987755982988, Calc.degreesToRadians(30), "Graus para radianos esta errado")
    

if __name__ == "__main__":
    unittest.main()