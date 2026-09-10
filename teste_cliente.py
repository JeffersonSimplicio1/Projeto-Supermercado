from models.cliente import Cliente
from servicos.cliente_servico import ClienteServico
from unittest.mock import Mock

servico = ClienteServico()

resultado = servico.excluir_por_nome("José")
print(resultado)
