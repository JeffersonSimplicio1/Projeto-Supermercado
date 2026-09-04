from repositorios.produtos_repositorios import ProdutoRepositorio

class ProdutoServico:
    def __init__(self):
        self.repositorio = ProdutoRepositorio()

    def cadastrar(self, produto):
        if produto.preco < 0 or produto.qtd_estoque < 0:
            print('Impossível cadastrar o produto.\n'
                      'Valores Negativos!')
        else:
            cadastrar_produto = self.repositorio.cadastrar(produto)
            if cadastrar_produto:
                print('Produto cadastrado com sucesso!!')
            else:
                print('Produto não cadastrado!')

    def listar_todos(self):
        produtos =self.repositorio.listar_todos()
        if len(produtos) >0:
            for produto in produtos:
                print(produto)
        else:
            print('Não há itens no estoque!')

    def atualizar(self, produto_id, produto):
        produto_existente = self.repositorio.buscar_id(produto_id)

        if produto_existente:
            if produto.preco < 0 or produto.qtd_estoque < 0:
                print('Impossível atualizar produtos com valores negativos')
            else:
                resultado = self.repositorio.atualizar(produto_id, produto)
                if resultado:
                    print('Produto atualizado!')
                else:
                    print("Impossível atualizar")
        else:
            print("Produto inexistente!")

    def excluir_por_nome(self, nome ):
        produtos_encontrados = self.repositorio.buscar_por_nome(nome)

        if len(produtos_encontrados) > 0:
            print(f"Existem {len(produtos_encontrados)} itens com esse nome ")
            pergunta = input('Você deseja excluir permanentemente todos os itens encontrados (S/N)? ')
            resposta = pergunta.upper().strip()
            if resposta == 'S':
                acao = self.repositorio.excluir_por_nome(nome)
                print(f'{acao} Itens Foram excluidos!')
            elif resposta == 'N':
                print('Ação cancelada! \n'
                      'Os itens permanecem no estoque!')
            else:
                print('Opção invalida! \n'
                      'Ação abortada!\n'
                      'Os itens permanecem no estoque!')

        else:
            print("Não há itens com esse nome!")

    def excluir_por_id(self, produto_id):
        id_encontrado = self.repositorio.buscar_id(produto_id)

        if id_encontrado:
            pergunta = input(f'O item de numero: {produto_id} foi encontrado. Tem certeza que deseja excluir (S/N)?')
            resposta = pergunta.upper().strip()
            if resposta == 'S':
                acao =self.repositorio.excluir_por_id(produto_id)
                if acao:
                    print('O item foi excluído!')
                else:
                    print('O item não pôde ser excluido')
            elif resposta == 'N':
                print('Operação cancelada!')
            else:
                print('Opção invalida!\n'
                      '!!! Operação CANCELADA !!!')
        else:
            print("Não existe item registrado com esse id")

