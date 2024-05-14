class Pessoa:
    def __init__(self, nome, idade):
        self.idade =  idade
        self.nome = nome
    
    def mostrar_dados(self):
        print(self.nome)
        print(self.idade)