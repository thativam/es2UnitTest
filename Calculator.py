import math


class Calculator:
    """
        Classe de uma calculadora simples para seminario sobre teste funcionais e suas ferramentas
    """
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError('Impossivel dividir por 0')
        return x / y
    def factorial(n):
        if( n < 0): 
            raise TypeError("Argumento do fatorial deve ser maior ou igual a 0")
        if n == 0:
            return 1
        else:
            return n * Calculator.factorial(n - 1)

    def sin(x, terms=10):
        """
        Calcula o seno com uma serie de taylor
    Args:
        x (float): Angulo em radianos.
        terms (int): numero de termos a ser usado na serie de Taylor
    """
        sine = 0
        for i in range(terms):
            sign = (-1) ** i
            sine += sign * (x ** (2 * i + 1)) / Calculator.factorial(2 * i + 1)
        return sine

    def cos(x, terms=10):
        """
        Calcula o cosseno com uma serie de taylor
    Args:
        x (float): Angulo em radianos.
        terms (int): numero de termos a ser usado na serie de Taylor
    """
        result = 0
        for n in range(terms):
            sign = (-1) ** n
            numerator = x ** (2 * n)
            denominator = Calculator.factorial(2 * n )
            result += (sign * numerator) / denominator
        return result

    def tan(x, terms=10):
        """
        Calcula a tangente usando tg = sin/cos.
    Args:
        x (float): Angulo em radianos.
        terms (int): numero de termos a ser usado na serie de Taylor
    """
        return Calculator.sin(x, terms) / Calculator.cos(x, terms)

    def degreesToRadians(degrees):
        return math.radians(degrees)

calc = Calculator()
print("Addition:", calc.add(5, 3))
print("Subtraction:", calc.subtract(5, 3))
print("Multiplication:", calc.multiply(5, 3))
print("Division:", calc.divide(9, 1))

degree = -60
radians = math.radians(degree) 
print("sin(" + str(degree) +"°):", format(Calculator.sin(radians),".4f"))
print("cos(" + str(degree) +"°):", format(Calculator.cos(radians),".4f"))
print("tan(" + str(degree) +"°):", format(Calculator.tan(radians),".4f"))

