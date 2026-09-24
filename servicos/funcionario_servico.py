from repositorios.funcionario_repositorio import FuncionarioRepositorio

class FuncionarioServico:
    def __init__(self):
        self.repositorio = FuncionarioRepositorio()
        self.salario_minimo = 1621.00

    def cadastrar(self, funcionario):
        if funcionario.nome.strip() and funcionario.cargo.strip():
            if funcionario.salario >= self.salario_minimo:
                cadastrar_funcionario = self.repositorio.cadastrar(funcionario)
                if cadastrar_funcionario:
                    msg = "Funcionário cadastrado com sucesso"
                else:
                    msg = ("Funcionário não cadastrado!\n"
                           "Erro no servidor!")
            else:
                msg = ("Informações de salário não permitida!\n"
                       "- Valor abaixo do minimo!")
        else:
            msg = ("Dados do funcionário incompleto(s)\n"
                   "Revise as informações e tente novamente!!!")
        return msg

    def listar_todos(self):
        listar_funcionarios = self.repositorio.listar_todos()
        if not listar_funcionarios:
            msg = "Não existe funcionários cadastrados"
        else:
            msg = listar_funcionarios
        return msg

    def buscar_por_id(self, matricula):
        buscar_funcionario = self.repositorio.buscar_por_id(matricula)
        if not buscar_funcionario:
            msg = "Não há funcionário cadastrado com essa matricula"
        else:
            msg = buscar_funcionario
        return msg

    def buscar_por_nome(self, nome):
        nome_tratado = nome.strip()
        if nome_tratado:
            buscar_funcionario = self.repositorio.buscar_por_nome(nome_tratado)
            if not buscar_funcionario:
                msg = "Não há funcionário cadastrado com este nome!"
            else:
                msg = buscar_funcionario
        else:
            msg = "Insira um valor no campo nome!"

        return msg

    def atualizar(self,matricula, funcionario):
        buscar = self.repositorio.buscar_por_id(matricula)
        if not buscar:
            msg = "Nenhum funcionário encontrado com essa matricula"
        else:
            if funcionario.nome.strip() and funcionario.cargo.strip():
                if funcionario.salario >= self.salario_minimo:
                    atualizar = self.repositorio.atualizar(matricula,funcionario)
                    if not atualizar:
                        msg = ("Impossível atualizar no momento!\n"
                               "- Erro no servidor!")
                    else:
                        msg = "Informações do funcionário atualizadas com sucesso!"
                else:
                    msg = ("Informações de salário incorretas\n"
                           "- O valor salarial esta abaixo do salário minimo!")
            else:
                msg = ("Dados do funcionário incompleto(s)\n"
                   "Revise as informações e tente novamente!!!")
        return msg

    def excluir_por_id(self,matricula):
        buscar = self.repositorio.buscar_por_id(matricula)
        if not buscar:
            msg = "Não existe funcionário com a matricula inserida!"
        else:
            excluir_funcionario = self.repositorio.excluir_por_id(matricula)
            if not excluir_funcionario:
                msg = ("Funcionário não excluído(a)!\n"
                       "Erro no servidor!")
            else:
                msg = "Ação bem sucedida!"
        return msg

    def excluir_por_nome(self, nome):
        nome_tratado = nome.strip()
        if nome_tratado:
            buscar = self.repositorio.buscar_por_nome(nome_tratado)
            if not buscar:
                msg = "Não há funcionario(s) cadastrado com esse nome"
            else:
                excluir = self.repositorio.excluir_por_nome(nome_tratado)
                if not excluir:
                    msg =("Impossivel excluir funcionario(s)\n"
                          "Erro no servidor!")
                else:
                    msg = "Ação bem sucedida!"
        else:
            msg = "Insira um valor no campo nome!"
        return msg



