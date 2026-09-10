from repositorios.cliente_repositorios import ClienteRepositorio

class ClienteServico:
    def __init__(self):
        self.repositorio = ClienteRepositorio()

    def cadastrar(self,cliente):
        if cliente.nome.strip() and cliente.cpf.strip():
            cadastrar_cliente =self.repositorio.cadastrar(cliente)
            if cadastrar_cliente:
                return 'Cliente cadastrado com sucesso!'
            else:
                return  "Cliente não cadastrado! (Resposta negativa do Banco de dados)"
        else:
            return "Por Favor, insira um valor valido nos campos Nome e Cpf!"

    def listar_todos(self):
        lista_clientes = self.repositorio.listar_todos()
        if not lista_clientes:
            return "Não existe clientes cadastrados!!"
        else:
            return lista_clientes

    def buscar_por_id(self,cliente_id):
        identificacao = self.repositorio.buscar_por_id(cliente_id)
        if not identificacao:
            return "ID inexistente!"
        else:
            return identificacao

    def buscar_por_nome(self, nome):
        busca = self.repositorio.buscar_por_nome(nome)
        if not busca:
            return "Não foram encontrados registros com esse nome"
        else:
           return busca

    def atualizar(self, cliente_id, cliente):
        buscar_cliente = self.repositorio.buscar_por_id(cliente_id)
        if not buscar_cliente:
            msg = "Id inexistente!"
        else:
            atualizar_dados = self.repositorio.atualizar(cliente_id, cliente)
            if not atualizar_dados:
                msg = ("Os dados não foram atualizados!\n"
                    "Erro interno!")
            else:
                msg = "Dados do cliente, Atualizado com SUCESSO!"
        return msg

    def excluir_por_id(self,cliente_id):
        cliente = self.repositorio.buscar_por_id(cliente_id)
        if not cliente:
            msg = 'O Id solicitado não foi encontrado!'
        else:
            excluir = self.repositorio.excluir_por_id(cliente_id)
            if not excluir:
                msg = ("Id não excluido!\n"
                       "Erro Interno!")
            else:
                msg = "Cliente excluido com Sucesso"
        return msg

    def excluir_por_nome(self, nome):
        cliente = self.repositorio.buscar_por_nome(nome)
        if not cliente:
            msg = "Nenhum cliente encontrado"
        else:
            excluir = self.repositorio.excluir_por_nome(nome)
            if not excluir:
                msg = ("Impossivel excluir\n"
                       "Erro Interno!")
            else:
                msg = "Cliente(s) excluido(s)"
        return msg