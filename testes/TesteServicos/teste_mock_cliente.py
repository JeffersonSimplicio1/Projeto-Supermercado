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
        self.mock_repositorio.cadastrar.return_value = True
        resultado = self.servico.cadastrar(cliente)
        self.mock_repositorio.cadastrar.assert_called_once_with(cliente)
        self.assertEqual(resultado,'Cliente cadastrado com sucesso!')

    def test_cadastrar_cliente_nomeCpf_em_branco(self):
        cliente = Cliente("","",819958756,"aaa@gmail.com")
        resultado = self.servico.cadastrar(cliente)
        self.mock_repositorio.cadastrar.assert_not_called()
        self.assertEqual(resultado, "Por Favor, insira um valor valido nos campos Nome e Cpf!")

    def test_cadastrar_cliente_nome_em_branco(self):
        cliente = Cliente("", "095.055.123.12", 819958756, "aaa@gmail.com")
        resultado = self.servico.cadastrar(cliente)
        self.mock_repositorio.cadastrar.assert_not_called()
        self.assertEqual(resultado, "Por Favor, insira um valor valido nos campos Nome e Cpf!")

    def test_cadastrar_cliente_cpf_em_branco(self):
        cliente = Cliente("Benjamin", "",8178956321,"ben10@hotmail.com")
        resultado = self.servico.cadastrar(cliente)
        self.mock_repositorio.cadastrar.assert_not_called()
        self.assertEqual(resultado, "Por Favor, insira um valor valido nos campos Nome e Cpf!")

    def test_cadastrar_cliente_erro_repositorio(self):
        cliente = Cliente("João", "098.050.987.66", 81998599798, "aaa@gmail.com")
        self.mock_repositorio.cadastrar.return_value = False
        resultado = self.servico.cadastrar(cliente)
        self.mock_repositorio.cadastrar.assert_called_once_with(cliente)
        self.assertEqual(resultado,"Cliente não cadastrado! (Resposta negativa do Banco de dados)")

    def test_listar_todos_sucesso(self):
        clientes = ["Cliente1", "Cliente2", "Cliente3"]
        self.mock_repositorio.listar_todos.return_value = clientes
        resultado = self.servico.listar_todos()
        self.mock_repositorio.listar_todos.assert_called_once_with ()
        self.assertEqual(resultado, clientes)

    def test_lista_todos_lista_vazia(self):
        self.mock_repositorio.listar_todos.return_value = []
        resultado = self.servico.listar_todos()
        self.mock_repositorio.listar_todos.assert_called_once_with()
        self.assertEqual(resultado, "Não existe clientes cadastrados!!")

    def test_buscar_por_id_existente(self):
        cliente = Cliente("Maria", "011.254.699-44")
        self.mock_repositorio.buscar_por_id.return_value = cliente
        resultado = self.servico.buscar_por_id(2)
        self.mock_repositorio.buscar_por_id.assert_called_once_with(2)
        self.assertEqual(resultado,f"Cliente: {cliente}")

    def test_buscar_por_id_inexistente(self):
        self.mock_repositorio.buscar_por_id.return_value = []
        resultado = self.servico.buscar_por_id(2)
        self.mock_repositorio.buscar_por_id.assert_called_once_with(2)
        self.assertEqual(resultado, "Cliente inexistente!")

    def test_buscar_por_nome_inexistente(self):
        self.mock_repositorio.buscar_por_nome.return_value=[]
        resultado = self.servico.buscar_por_nome("Jefferson")
        self.mock_repositorio.buscar_por_nome.assert_called_once_with("Jefferson")
        self.assertEqual(resultado, "Não foram encontrados registros com esse nome")

    def test_buscar_por_nome_existente(self):
        cliente = Cliente("Jefferson", "254.568.555-98",8195785455, "ccc@hotmail.com")
        self.mock_repositorio.buscar_por_nome.return_value = cliente
        resultado = self.servico.buscar_por_nome("Jefferson")
        self.mock_repositorio.buscar_por_nome.assert_called_once_with("Jefferson")
        self.assertEqual(resultado,cliente)

    def test_buscar_por_nome_nome_vazio(self):
        cliente = Cliente('','098.145.689-66',34447985, 'www@email.com')
        resultado = self.servico.buscar_por_nome("")
        self.mock_repositorio.buscar_por_nome.assert_not_called()
        self.assertEqual(resultado,"Insira um nome para iniciar a pesquisa!")

