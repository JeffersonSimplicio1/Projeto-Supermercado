from repositorios.produtos_repositorios import ProdutoRepositorio

repositorio = ProdutoRepositorio()

produtos= repositorio.listar_todos()

for produto in produtos:
    print(produto)
