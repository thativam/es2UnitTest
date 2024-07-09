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
    def factorial(self,n):
        if( n < 0): 
            raise TypeError("Argumento do fatorial deve ser maior ou igual a 0")
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def sin(self,x, terms=10):
        """
        Calcula o seno com uma serie de taylor
    Args:
        x (float): Angulo em radianos.
        terms (int): numero de termos a ser usado na serie de Taylor
    """
        sine = 0
        for i in range(terms):
            sign = (-1) ** i
            sine += sign * (x ** (2 * i + 1)) / self.factorial(2 * i + 1)
        return sine

    def cos(self,x, terms=10):
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
            denominator = self.factorial(2 * n )
            result += (sign * numerator) / denominator
        return result

    def tan(self,x, terms=10):
        """
        Calcula a tangente usando tg = sin/cos.
    Args:
        x (float): Angulo em radianos.
        terms (int): numero de termos a ser usado na serie de Taylor
    """
        return self.sin(x, terms) / self.cos(x, terms)

    def degreesToRadians(self,degrees):
        return math.radians(degrees)

def main():
    calc = Calculator()
    while True:
        print("Escolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Seno")
        print("6 - Cosseno")
        print("7 - Tangente")
        print("8 - Fatorial")
        print("9 - Converter graus para radianos")
        print("0 - Sair")

        choice = input("Digite o número da operação desejada: ")

        if choice == '0':
            print("Encerrando a calculadora.")
            break

        if choice in ['1', '2', '3', '4']:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))

        if choice == '1':
            print(f"Resultado: {calc.add(x, y)}")
        elif choice == '2':
            print(f"Resultado: {calc.subtract(x, y)}")
        elif choice == '3':
            print(f"Resultado: {calc.multiply(x, y)}")
        elif choice == '4':
            try:
                print(f"Resultado: {calc.divide(x, y)}")
            except ZeroDivisionError as e:
                print(e)
        elif choice == '5':
            angle = float(input("Digite o ângulo em graus: "))
            radians = calc.degreesToRadians(angle)
            print(f"Seno({angle}°): {calc.sin(radians)}")
        elif choice == '6':
            angle = float(input("Digite o ângulo em graus: "))
            radians = calc.degreesToRadians(angle)
            print(f"Cosseno({angle}°): {calc.cos(radians)}")
        elif choice == '7':
            angle = float(input("Digite o ângulo em graus: "))
            radians = calc.degreesToRadians(angle)
            print(f"Tangente({angle}°): {calc.tan(radians)}")
        elif choice == '8':
            n = int(input("Digite um número inteiro não negativo: "))
            try:
                print(f"Fatorial({n}): {calc.factorial(n)}")
            except TypeError as e:
                print(e)
        elif choice == '9':
            degrees = float(input("Digite o ângulo em graus: "))
            print(f"{degrees} graus em radianos: {calc.degreesToRadians(degrees)}")
        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    main()

