from servicos.produto_servico import ProdutoServico
from repositorios.produtos_repositorios import ProdutoRepositorio
from models.produto import Produto

novo_prod = Produto('Alimento', 'Macarrão 500g', 25.15 ,150)

servicos = ProdutoServico()

servicos.atualizar(11,novo_prod)