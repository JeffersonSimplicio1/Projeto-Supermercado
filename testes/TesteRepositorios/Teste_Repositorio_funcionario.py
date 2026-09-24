from repositorios.funcionario_repositorio import FuncionarioRepositorio
from models.Funcionario import Funcionario

repositorio = FuncionarioRepositorio()
colaborador1= Funcionario("Sophia", "Marketing", 3000.00)

# matricula = repositorio.cadastrar(colaborador)
# print(matricula)

# buscarId = repositorio.buscar_por_id(10)
# print(buscarId)

# buscarFuncionario = repositorio.buscar_por_nome("Sophia")
# print(buscarFuncionario)

# listar = repositorio.listar_todos()
# print(listar)

# atualize = repositorio.atualizar(19,colaborador1)
# print(atualize)

# excluirMatricula = repositorio.excluir_por_id(10)
# print(excluirMatricula)

# excluirFunc =repositorio.excluir_por_nome("Andreia")
# print(excluirFunc)