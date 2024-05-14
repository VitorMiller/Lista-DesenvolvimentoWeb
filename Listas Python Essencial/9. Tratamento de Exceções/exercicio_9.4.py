class SaldoInsuficiente(Exception):
    def __init__(self):
        super().__init__("Saldo insuficiente")

class Conta_Bancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficiente()
        self.saldo -= valor

conta = Conta_Bancaria(1000)

try:
    conta.sacar(100)
    print(conta.saldo)
    conta.sacar(2000)
except SaldoInsuficiente as e:
    print(e)