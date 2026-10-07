from repositorios.vendas_repositorios import VendaRepositorio
from repositorios.cliente_repositorios import ClienteRepositorio
from repositorios.funcionario_repositorio import FuncionarioRepositorio
from models.vendas import Vendas


class VendaServico:
    def __init__(self):
        self.repositorioVenda = VendaRepositorio()
        self.repositorioCliente = ClienteRepositorio()
        self.repositorioFuncionario = FuncionarioRepositorio()

    def cadastrar(self, funcionario_id, cliente_id=None):
        if funcionario_id is None:
            msg = 'Funcionario não informado!'
        else:
            buscar_funcionario = self.repositorioFuncionario.buscar_por_id(funcionario_id)
            if buscar_funcionario:
                if cliente_id is not None:
                    buscar_cliente = self.repositorioCliente.buscar_por_id(cliente_id)
                    if buscar_cliente:
                        nova_venda = Vendas(funcionario_id, cliente_id)
                        venda_id = self.repositorioVenda.cadastrar(nova_venda)
                        msg = (f"Seja Bem Vindo!\n"
                               f"Carrinho Aberto!\n"
                               f"ID do carrinho: {venda_id}\n"
                               f"Adicione itens no carrinho!")
                    else:
                        msg = 'Cliente não encontrado.'
                else:
                    nova_venda = Vendas(funcionario_id, cliente_id)
                    venda_id = self.repositorioVenda.cadastrar(nova_venda)
                    msg = (f"Cliente Anônimo\n"
                           f"Seja Bem Vindo!\n"
                           f"Carrinho Aberto!\n"
                           f"ID do carrinho: {venda_id}\n"
                           f"Adicione itens no carrinho!")
            else:
                 msg = "Funcionário não encontrado!"

        return msg


venda = VendaServico()
venda1 = venda.cadastrar(2,10)
venda2 = venda.cadastrar(2)