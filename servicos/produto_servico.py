from repositorios.produtos_repositorios import ProdutoRepositorio

class ProdutoServico:
    def __init__(self):
        self.repositorio = ProdutoRepositorio()

    def cadastrar(self, produto):
        if produto.preco < 0 or produto.qtd_estoque < 0:
            msg =( "Impossível cadastrar o produto.\n"
                      " Valores Negativos!")
        else:
            cadastrar_produto = self.repositorio.cadastrar(produto)
            if cadastrar_produto:
                msg = ('Produto cadastrado com sucesso!!')
            else:
                msg = ('Produto não cadastrado!')
        return msg

    def listar_todos(self):
        produtos =self.repositorio.listar_todos()
        if len(produtos) >0:
            for produto in produtos:
                msg = produto
        else:
            msg ='Não há itens no estoque!'
        return msg

    def atualizar(self, produto_id, produto):
        produto_existente = self.repositorio.buscar_id(produto_id)

        if produto_existente:
            if produto.preco < 0 or produto.qtd_estoque < 0:
                msg ='Impossível atualizar produtos com valores negativos'
            else:
                resultado = self.repositorio.atualizar(produto_id, produto)
                if resultado:
                    msg ='Produto atualizado!'
                else:
                    msg ="Impossível atualizar"
        else:
            msg ="Produto inexistente!"
        return msg

    def excluir_por_nome(self, nome ):
        produtos_encontrados = self.repositorio.buscar_por_nome(nome)
        if not produtos_encontrados:
            msg = "Nenhum Produto encontrado."
        else:
            excluir = self.repositorio.excluir_por_nome(nome)
            if not excluir:
                msg = ("Impossivel excluir Produto(s)\n"
                       "Erro Interno!")
            else:
                msg = "Produto(s) excluido(s) com Sucesso!"
        return msg

    def excluir_por_id(self,  produto_id):
        id_encontrado = self.repositorio.buscar_id(produto_id)
        if not id_encontrado:
            msg = "Nenhum produto encontrado com esse ID "
        else:
            excluir = self.repositorio.excluir_por_id(produto_id)
            if not excluir:
                msg = ("Impossivel excluir Produto\n"
                       "Erro Interno!")
            else:
                msg = "Produto excluido com Sucesso!"
        return msg


