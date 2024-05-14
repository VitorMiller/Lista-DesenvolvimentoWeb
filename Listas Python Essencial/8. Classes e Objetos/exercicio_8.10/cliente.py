#pessoa + endereço
from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade)
        self.endereco = endereco
    
    def mostrar_dados(self):
        print(self.nome)
        print(self.idade)
        print(self.endereco)
        