from database.coneccao import criar_conexao

class ClienteRepositorio:
    def cadastrar(self, cliente):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        try:
            sql = """INSERT INTO cliente (nome, cpf, telefone, email) VALUES (%s, %s, %s, %s)"""

            valores = (
                cliente.nome,
                cliente.cpf,
                cliente.telefone,
                cliente.email
            )

            cursor.execute(sql, valores)
            cliente_id = cursor.lastrowid

            conexao.commit()
            return  cliente_id
        finally:
            cursor.close()
            conexao.close()

    def buscar_por_id(self, cliente_id):

        try:
            conexao =criar_conexao()
            cursor = conexao.cursor()

            sql = """SELECT * FROM supermercado.cliente WHERE id = %s"""

            cursor.execute(sql,(cliente_id, ))
            clientes = cursor.fetchone()
            return clientes
        finally:
            cursor.close()
            conexao.close()

    def buscar_por_nome(self, nome):
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """SELECT * FROM supermercado.cliente WHERE nome = %s"""

            cursor.execute(sql, (nome, ))
            clientes = cursor.fetchall()
            return clientes
        finally:
            cursor.close()
            conexao.close()

    def listar_todos(self):
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """SELECT ID, nome, cpf, telefone, email FROM cliente"""

            cursor.execute(sql)
            clientes = cursor.fetchall()
            return clientes
        finally:
            cursor.close()
            conexao.close()

    def atualizar(self, cliente_id,cliente):

        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """UPDATE cliente SET nome = %s, cpf = %s, telefone = %s, email = %s WHERE id = %s"""

            valores = (
                cliente.nome,
                cliente.cpf,
                cliente.telefone,
                cliente.email,
                cliente_id
            )

            cursor.execute(sql, valores)
            quantidade = cursor.rowcount
            conexao.commit()
            return quantidade > 0
        finally:
            cursor.close()
            conexao.close()

    def excluir_por_id(self, cliente_id):
           try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """ DELETE FROM supermercado.cliente WHERE ID = %s"""

            valores =(cliente_id, )

            cursor.execute(sql, valores)
            quantidade = cursor.rowcount

            conexao.commit()
            return quantidade > 0
           finally:
               cursor.close()
               conexao.close()

    def excluir_por_nome(self, nome):
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """DELETE FROM supermercado.cliente WHERE nome = %s"""

            valores = (nome, )

            cursor.execute(sql, valores)

            quantidade = cursor.rowcount
            conexao.commit()
            return quantidade
        finally:
            cursor.close()
            conexao.close()






