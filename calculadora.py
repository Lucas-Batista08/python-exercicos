class Calculadora:
    @staticmethod
    def multiplicacao(a,b):
        return a *b
calculadora =Calculadora()
resultado = calculadora.multiplicacao(5,7)
print("resultado da multiplicação:", resultado)