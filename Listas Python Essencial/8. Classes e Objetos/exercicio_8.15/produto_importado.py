from produto import Produto
class Produto_Importado(Produto):
    def __init__(self, nome, preco, qtd_estoque, imposto):
        super().__init__(nome, preco, qtd_estoque)
        self.imposto = imposto

    def preco_final(self):
        print(self.preco+(self.preco*self.imposto))