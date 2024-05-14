class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def mostrar_dados(self):
        print(f"{self.numerador}/{self.denominador}")

    def multiplicar(self, fracao2):
        resultado_numerador = self.numerador*fracao2.numerador
        resultado_denominador = self.denominador*fracao2.denominador
        return Fracao(resultado_numerador, resultado_denominador)