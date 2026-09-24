import unittest
from unittest.mock import Mock
from servicos.produto_servico import ProdutoServico
from models.produto import Produto


class TestProdutoServico(unittest.TestCase):
    def setUp(self):
        self.servico = ProdutoServico()
        self.mock_repositorio = Mock()
        self.servico.repositorio = self.mock_repositorio

    def test_cadastrar_produto_sucesso(self):
        produto = Produto("Refrigerante", 12.00,60, "Bebida")
        self.mock_repositorio.cadastrar.return_value = True
        resultado = self.servico.cadastrar(produto)
        self.mock_repositorio.cadastrar.assert_called_once_with(produto)
        self.assertEqual(resultado,'Produto cadastrado com sucesso!!')

    def test_cadastrar_produto_falha(self):
        produto = Produto('Maçã 1Kg', 5.00, 200, 'Frutas'   )
        self.mock_repositorio.cadastrar.return_value = False
        resultado = self.servico.cadastrar(produto)
        self.mock_repositorio.cadastrar.assert_called_once_with(produto)
        self.assertEqual(resultado, 'Produto não cadastrado!')

    def test_cadastrar_produto_valores_negativos(self):
        produto = Produto('Melancia 1Kg', -2.20, 400, 'Frutas' )
        resultado = self.servico.cadastrar(produto)
        self.mock_repositorio.cadastrar.assert_not_called()
        self.assertEqual(resultado,"Impossível cadastrar o produto.\n"
                      " Valores Negativos!")

    def test_listar_todos(self):
        produtos = [("Alimentos", "Arroz", 5.90, 10), ("Bebida", "Coca-Cola", 11.00, 20)]
        self.mock_repositorio.listar_todos.return_value = produtos
        resultado = self.servico.listar_todos()
        self.mock_repositorio.listar_todos.assert_called_once_with()
        self.assertEqual(resultado, produtos)

    def test_listar_todos_sem_produtos(self):
        self.mock_repositorio.listar_todos.return_value = []
        resultado = self.servico.listar_todos()
        self.mock_repositorio.listar_todos.assert_called_once_with()
        self.assertEqual(resultado, 'Não há itens no estoque!')

    def test_buscar_id_existente(self):
        produto = Produto("Refrigerante", 12.00,60, "Bebida")
        self.mock_repositorio.buscar_id.return_value = produto
        resultado = self.servico.buscar_por_id(1)
        self.mock_repositorio.buscar_id.assert_called_once_with(1)
        self.assertEqual(resultado,  f'Produto: {produto}')

    def test_buscar_id_inexistente(self):
        produto = Produto( "Refrigerante", 12.00,60, "Bebida")
        self.mock_repositorio.buscar_id.return_value = []
        resultado = self.servico.buscar_por_id(1)
        self.mock_repositorio.buscar_id.assert_called_once_with(1)
        self.assertEqual(resultado, "Produto inexistente")

    def test_buscar_por_nome_produtos_encontrados(self):
        self.mock_repositorio.buscar_por_nome.return_value = ["produto 1","produto 2","produto 3"]

        resultado = self.servico.buscar_por_nome("Macarrão 500g")
        self.mock_repositorio.buscar_por_nome.assert_called_once_with("Macarrão 500g")
        self.assertEqual(resultado,["produto 1","produto 2","produto 3"])

    def test_buscar_por_nome_sem_resultado(self):
        self.mock_repositorio.buscar_por_nome.return_value = []
        resultado = self.servico.buscar_por_nome("Café")
        self.mock_repositorio.buscar_por_nome.assert_called_once_with("Café")
        self.assertEqual(resultado, "Não há registros de produtos com o nome solicitado")

    def test_buscar_por_nome_nome_vazio(self):
        resultado = self.servico.buscar_por_nome("")
        self.mock_repositorio.buscar_por_nome.assert_not_called()
        self.assertEqual(resultado, "Insira um nome para iniciar a pesquisa!")

    def test_atualizar_produto_existente_sucesso(self):
        self.mock_repositorio.buscar_id.return_value = 1
        self.mock_repositorio.atualizar.return_value = True
        produto = Produto("Leite", 5.90, 20,"Bebida")
        resultado = self.servico.atualizar(1, produto)
        self.mock_repositorio.buscar_id.assert_called_once_with(1)
        self.mock_repositorio.atualizar.assert_called_once_with(1, produto)
        self.assertEqual(resultado, 'Produto atualizado!')

    def test_atualizar_produto_existente_falha_repositorio(self):
        produto = Produto('Café', 12.98,100,"Bebida" )
        self.mock_repositorio.buscar_id.return_value = 2
        self.mock_repositorio.atualizar.return_value = False
        resultado = self.servico.atualizar(2,produto)
        self.mock_repositorio.buscar_id.assert_called_once_with(2)
        self.mock_repositorio.atualizar.assert_called_once_with(2, produto)
        self.assertEqual(resultado,"Impossível atualizar")

    def test_atualizar_produto_valores_negativos(self):
        produto = Produto("Feijão", -8.60, 100,"Alimento")
        self.mock_repositorio.buscar_id.return_value = 5
        self.mock_repositorio.atualizar.return_value = True
        resultado = self.servico.atualizar(5, produto)
        self.mock_repositorio.buscar_id.assert_called_once_with(5)
        self.mock_repositorio.assert_not_called()
        self.assertEqual(resultado,'Impossível atualizar produtos com valores negativos')

    def test_atualizar_produto_inexistente(self):
        produto = Produto("Nescau", 3.29, 50, "Bebida")
        self.mock_repositorio.buscar_id.return_value =False
        resultado = self.servico.atualizar(5,produto)
        self.mock_repositorio.buscar_id.assert_called_once_with(5)
        self.mock_repositorio.atualizar.assert_not_called()
        self.assertEqual(resultado, 'Produto inexistente!')

    def test_excluir_por_nome_sucesso(self):
        self.mock_repositorio.buscar_por_nome.return_value = ["nome1","nome2","nome3"]
        self.mock_repositorio.excluir_por_nome.return_value = True
        resultado = self.servico.excluir_por_nome("nome")
        self.mock_repositorio.excluir_por_nome.assert_called_once_with("nome")
        self.assertEqual(resultado,"Produto(s) excluido(s) com Sucesso!")

    def test_excluir_por_nome_inexistente(self):
        self.mock_repositorio.buscar_por_nome.return_value = []
        self.mock_repositorio.excluir_por_nome.return_value = False
        resultado = self.servico.excluir_por_nome("nome")
        self.mock_repositorio.excluir_por_nome.assert_not_called()
        self.assertEqual(resultado, "Nenhum Produto encontrado.")

    def test_excluir_por_nome_falha_no_repositorio(self):
        self.mock_repositorio.buscar_por_nome.return_value = ["nome1","nome2","nome3"]
        self.mock_repositorio.excluir_por_nome.return_value = False
        resultado = self.servico.excluir_por_nome("nome")
        self.mock_repositorio.excluir_por_nome.assert_called_once_with("nome")
        self.assertEqual(resultado, "Impossivel excluir Produto(s)\n"
                       "Erro Interno!")

    def test_excluir_por_id_sucesso(self):
        produto = Produto("Trigo", 4.59, 50, "Alimento")
        self.mock_repositorio.buscar_id.return_value = produto
        self.mock_repositorio.excluir_por_id.return_value = True
        resultado= self.servico.excluir_por_id(10)
        self.mock_repositorio.buscar_id.assert_called_once_with(10)
        self.assertEqual(resultado,"Produto excluido com Sucesso!")

    def test_excluir_por_id_inexistente(self):
        self.mock_repositorio.buscar_id.return_value = []
        resultado = self.servico.excluir_por_id(12)
        self.mock_repositorio.excluir_por_id.assert_not_called()
        self.assertEqual(resultado,"Nenhum produto encontrado com esse ID ")

    def test_excluir_por_id_falha_no_repositorio(self):
        self.mock_repositorio.buscar_id.return_value = ['produto 1','produto 2','produto 3']
        self.mock_repositorio.excluir_por_id.return_value = False
        resultado = self.servico.excluir_por_id(5)
        self.mock_repositorio.excluir_por_id.assert_called_once_with(5)
        self.assertEqual(resultado,"Impossivel excluir Produto\n"
                       "Erro Interno!")


if __name__ == "__main__":
    unittest.main()



