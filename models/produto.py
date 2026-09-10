class Produto:
    def __init__(self,nome, preco,qtd_estoque,categoria = None):
        self.categoria = categoria
        self.nome = nome
        self.preco = preco
        self.qtd_estoque = qtd_estoque
