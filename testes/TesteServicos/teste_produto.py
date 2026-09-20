from servicos.produto_servico import ProdutoServico
# from repositorios.produtos_repositorios import ProdutoRepositorio
# from models.produto import Produto
from unittest.mock import Mock

# novo_prod = Produto('Alimento', 'Macarrão 500g', 25.15 ,150)
servico = ProdutoServico()

mock_repositorio = Mock()
servico.repositorio = mock_repositorio

mock_repositorio.buscar_por_nome.return_value = []
resultado = servico.buscar_por_nome("Feijão")
# mock_repositorio.buscar_por_nome.assert_not_called()
# mock_repositorio.buscar_por_nome.assert_called_once_with("Feijão")

print(resultado)
