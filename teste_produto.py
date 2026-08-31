from repositorios.produtos_repositorios import ProdutoRepositorio
from models.produto import Produto

repositorio = ProdutoRepositorio()

produto_atualizado = Produto("Limpeza","Detergente 500ml", 3.00,100)

if repositorio.excluir(7):
    print("Item excluido com sucesso!!")
else:
    print("Produto não encontrado!")