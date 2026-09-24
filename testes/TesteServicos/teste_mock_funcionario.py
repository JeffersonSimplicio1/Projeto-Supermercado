import unittest
from unittest.mock import Mock
from servicos.funcionario_servico import FuncionarioServico
from models.Funcionario import Funcionario


class TestFuncionarioServico(unittest.TestCase):
    def setUp(self):
        self.servico = FuncionarioServico()
        self.mock_repositorio = Mock()
        self.servico.repositorio = self.mock_repositorio

    def test_cadastrar_funcionario_sucesso(self):
        funcionario = Funcionario("João", "Estoquista", 2500)
        self.mock_repositorio.cadastrar.return_value = True
        resultado = self.servico.cadastrar(funcionario)
        self.mock_repositorio.cadastrar.assert_called_once_with(funcionario)
        self.assertEqual(resultado, "Funcionário cadastrado com sucesso")

    def test_cadastrar_funcionario_valor_salario_invalido(self):
        funcionario = Funcionario("João", "Estoquista", 500)
        self.mock_repositorio.cadastrar.return_value = False
        resultado = self.servico.cadastrar(funcionario)
        self.mock_repositorio.cadastrar.assert_not_called()
        self.assertEqual(resultado, "Informações de salário não permitida!\n"
                       "- Valor abaixo do minimo!")

    def test_cadastrar_funcionario_valor_nome_invalido(self):
        funcionario = Funcionario(" ", "Estoquista", 2500)
        self.mock_repositorio.cadastrar.return_value = False
        resultado = self.servico.cadastrar(funcionario)
        self.mock_repositorio.cadastrar.assert_not_called()
        self.assertEqual(resultado,"Dados do funcionário incompleto(s)\n"
                   "Revise as informações e tente novamente!!!")

    def test_cadastrar_funcionario_valor_cargo_invalido(self):
        funcionario = Funcionario("João", "   ", 2500)
        self.mock_repositorio.cadastrar.return_value = False
        resultado = self.servico.cadastrar(funcionario)
        self.mock_repositorio.cadastrar.assert_not_called()
        self.assertEqual(resultado,"Dados do funcionário incompleto(s)\n"
                   "Revise as informações e tente novamente!!!")

    def test_cadastrar_funcionario_erro_servidor(self):
        funcionario = Funcionario("João", "Estoquista", 2500)
        self.mock_repositorio.cadastrar.return_value = False
        resultado = self.servico.cadastrar(funcionario)
        self.mock_repositorio.cadastrar.assert_called_once_with(funcionario)
        self.assertEqual(resultado,"Funcionário não cadastrado!\n"
                           "Erro no servidor!")

    def test_listar_todos_funcionarios_lista_vazia(self):
        self.mock_repositorio.listar_todos.return_value = []
        resultado = self.servico.listar_todos()
        self.mock_repositorio.listar_todos.assert_called_once_with()
        self.assertEqual(resultado, "Não existe funcionários cadastrados")

    def test_listar_todos_funcionarios_sucesso(self):
        lista = ["Nome1","Nome2","Nome3"]
        self.mock_repositorio.listar_todos.return_value = lista
        resultado = self.servico.listar_todos()
        self.mock_repositorio.listar_todos.assert_called_once_with()
        self.assertEqual(resultado, lista)

    def test_buscar_funcionario_por_id_sucesso(self):
        funcionario = Funcionario("João", "Estoquista", 2500)
        self.mock_repositorio.buscar_por_id.return_value = funcionario
        resultado = self.servico.buscar_por_id(3)
        self.mock_repositorio.buscar_por_id.assert_called_once_with(3)
        self.assertEqual(resultado, funcionario)

    def test_buscar_funcionario_por_id_inexistente(self):
        self.mock_repositorio.buscar_por_id.return_value = []
        resultado = self.servico.buscar_por_id(3)
        self.mock_repositorio.buscar_por_id.assert_called_once_with(3)
        self.assertEqual(resultado,"Não há funcionário cadastrado com essa matricula")

    def test_buscar_funcionario_por_nome_sucesso(self):
        lista_nome = ["Nome1","Nome2","Nome3"]
        self.mock_repositorio.buscar_por_nome.return_value = lista_nome
        resultado = self.servico.buscar_por_nome("Nome")
        self.mock_repositorio.buscar_por_nome.assert_called_once_with("Nome")
        self.assertEqual(resultado, lista_nome)

    def test_buscar_funcionario_por_nome_em_branco(self):
        resultado = self.servico.buscar_por_nome("  ")
        self.mock_repositorio.buscar_por_nome.assert_not_called()
        self.assertEqual(resultado,"Insira um valor no campo nome!")

    def test_buscar_funcionario_por_nome_inexistente(self):
        self.mock_repositorio.buscar_por_nome.return_value = False
        resultado = self.servico.buscar_por_nome("Nome")
        self.mock_repositorio.buscar_por_nome.assert_called_once_with("Nome")
        self.assertEqual(resultado,"Não há funcionário cadastrado com este nome!")

if __name__ == "__main__":
    unittest.main()