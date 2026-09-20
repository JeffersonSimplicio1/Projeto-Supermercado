import  unittest
from unittest.mock import Mock
from servicos.cliente_servico import ClienteServico
from models.cliente import Cliente


class TestClienteServico(unittest.TestCase):
    def setUp(self):
        self.servico = ClienteServico()
        self.mock_repositorio = Mock()
        self.servico.repositorio = self.mock_repositorio

    def test_cadastrar_cliente_sucesso(self):
        cliente = Cliente("João", "098.050.987.66",81998599798, "aaa@gmail.com")
        self.mock_repositorio.cadastrar.return_value = cliente
        resultado = self.servico.cadastrar(cliente)
        self.mock_repositorio.cadastrar.assert_called_once_with(cliente)
        self.assertEqual(resultado,'Cliente cadastrado com sucesso!')
    def test_cadastrar_cliente_nomeCpf_em_branco(self):
        cliente = Cliente("","",819958756,"aaa@gmail.com")
        resultado = self.servico.cadastrar(cliente)
        self.mock_repositorio.cadastrar.assert_not_called()
        self.assertEqual(resultado, "Por Favor, insira um valor valido nos campos Nome e Cpf!")

    def test_cadastrar_cliente_erro_repositorio(self):
        cliente = Cliente("João", "098.050.987.66", 81998599798, "aaa@gmail.com")
        self.mock_repositorio.cadastrar.return_value = False
        resultado = self.servico.cadastrar(cliente)
        self.mock_repositorio.cadastrar.assert_called_once_with(cliente)
        self.assertEqual(resultado,"Cliente não cadastrado! (Resposta negativa do Banco de dados)")


