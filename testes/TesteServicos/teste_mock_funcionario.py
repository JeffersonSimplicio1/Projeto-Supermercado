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

    def test_atualizar_funcionarios_sucesso(self):
        funcionario = Funcionario("Jefferson", "Gerente", 5000)
        self.mock_repositorio.buscar_por_id.return_value = 3
        self.mock_repositorio.atualziar.return_value = True
        resultado = self.servico.atualizar(3, funcionario)
        self.mock_repositorio.buscar_por_id.assert_called_once_with(3)
        self.mock_repositorio.atualizar.assert_called_once_with(3, funcionario)
        self.assertEqual(resultado, "Informações do funcionário atualizadas com sucesso!")

    def test_atualizar_funcionarios_erro_salario_abaixo_do_minimo(self):
        funcionario = Funcionario("Gabriel", "Caixa", 200)
        self.mock_repositorio.buscar_por_id.return_value = 3
        resultado = self.servico.atualizar(3,funcionario)
        self.mock_repositorio.buscar_por_id.assert_called_once_with(3)
        self.mock_repositorio.atualizar.assert_not_called()
        self.assertEqual(resultado, ("Informações de salário incorretas\n"
                           "- O valor salarial esta abaixo do salário minimo!"))

    def test_atualizar_funcionarios_erro_nome_em_branco(self):
        funcionario = Funcionario("  ", "Estoque",1800 )
        self.mock_repositorio.buscar_por_id.return_value = 3
        resultado = self.servico.atualizar(3,funcionario)
        self.mock_repositorio.atualizar.assert_not_called()
        self.assertEqual(resultado, "Dados do funcionário incompleto(s)\n"
                   "Revise as informações e tente novamente!!!")

    def test_atualizar_funcionarios_erro_cargo_em_branco(self):
        funcionario = Funcionario("Matheus", " ",1800 )
        self.mock_repositorio.buscar_por_id.return_value = 3
        resultado = self.servico.atualizar(3,funcionario)
        self.mock_repositorio.atualizar.assert_not_called()
        self.assertEqual(resultado, "Dados do funcionário incompleto(s)\n"
                   "Revise as informações e tente novamente!!!")

    def test_atualizar_funcionarios_erro_repositorio(self):
        funcionario = Funcionario("Gabriel", "Caixa", 2000)
        self.mock_repositorio.buscar_por_id.return_value = 3
        self.mock_repositorio.atualizar.return_value = False
        resultado = self.servico.atualizar(3,funcionario)
        self.mock_repositorio. buscar_por_id.assert_called_once_with(3)
        self.mock_repositorio.atualizar.assert_called_once_with(3,funcionario)
        self.assertEqual(resultado, "Impossível atualizar no momento!\n"
                               "- Erro no servidor!")

    def test_excluir_por_id_Sucesso(self):
        self.mock_repositorio.buscar_por_id.return_value = 3
        self.mock_repositorio.excluir_por_id.return_value = True
        resultado = self.servico.excluir_por_id(3)
        self.mock_repositorio.buscar_por_id.assert_called_once_with(3)
        self.mock_repositorio.excluir_por_id.assert_called_once_with(3)
        self.assertEqual(resultado, "Ação bem sucedida!")

    def test_excluir_por_id_inexistente(self):
        self.mock_repositorio.buscar_por_id.return_value = []
        self.mock_repositorio.excluir_por_id.return_value = 3
        resultado = self.servico.excluir_por_id(3)
        self.mock_repositorio.buscar_por_id.assert_called_once_with(3)
        self.mock_repositorio.excluir_por_id.assert_not_called()
        self.assertEqual(resultado,"Não existe funcionário com a matricula inserida!")

    def test_excluir_por_id_erro_no_repositorio(self):
        self.mock_repositorio.buscar_por_id.return_value= 3
        self.mock_repositorio.excluir_por_id.return_value = False
        resultado = self.servico.excluir_por_id(3)
        self.mock_repositorio.buscar_por_id.assert_called_once_with(3)
        self.mock_repositorio.excluir_por_id.assert_called_once_with(3)
        self.assertEqual(resultado,"Funcionário não excluído(a)!\n"
                       "Erro no servidor!")

    def test_excluir_por_nome_sucesso(self):
        lista = ["Nome1","Nome2","Nome3"]
        self.mock_repositorio.buscar_por_nome.return_value = lista
        self.mock_repositorio.excluir_por_nome.return_value = True
        resultado = self.servico.excluir_por_nome("Nome")
        self.mock_repositorio.buscar_por_nome.assert_called_once_with("Nome")
        self.mock_repositorio.excluir_por_nome.assert_called_once_with("Nome")
        self.assertEqual(resultado, "Ação bem sucedida!")

    def test_excluir_por_nome_inexistente(self):
        self.mock_repositorio.buscar_por_nome.return_value = []
        self.mock_repositorio.excluir_por_nome.return_value = False
        resultado = self.servico.excluir_por_nome("Nome")
        self.mock_repositorio.buscar_por_nome.assert_called_once_with("Nome")
        self.mock_repositorio.excluir_por_nome.assert_not_called()
        self.assertEqual(resultado, "Não há funcionario(s) cadastrado com esse nome")

    def test_excluir_por_nome_nome_em_branco(self):
        self.mock_repositorio.buscar_por_nome.return_value = False
        self.mock_repositorio.excluir_por_nome.return_value = False
        resultado = self.servico.excluir_por_nome("  ")
        self.mock_repositorio.buscar_por_nome.assert_not_called()
        self.mock_repositorio.excluir_por_nome.assert_not_called()
        self.assertEqual(resultado, "Insira um valor no campo nome!")

    def test_excluir_por_nome_erro_repositorio(self):
        self.mock_repositorio.excluir_por_nome.return_value = False
        resultado = self.servico.excluir_por_nome("Nome")
        self.mock_repositorio.buscar_por_nome.assert_called_once_with("Nome")
        self.mock_repositorio.excluir_por_nome.assert_called_once_with("Nome")
        self.assertEqual(resultado, "Impossivel excluir funcionario(s)\n"
                          "Erro no servidor!")



if __name__ == "__main__":
    unittest.main()