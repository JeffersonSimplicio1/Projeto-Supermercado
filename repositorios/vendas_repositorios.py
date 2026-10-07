from database.coneccao import criar_conexao

class VendaRepositorio:
    def cadastrar(self, venda):

        conexao = None
        cursor = None

        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql ="""INSERT INTO vendas (funcionario_id, cliente_id) VALUES (%s,%s)"""

            valores = (
                venda.funcionario_id,
                venda.cliente_id
            )

            cursor.execute(sql,valores)
            venda_id = cursor.lastrowid

            conexao.commit()
            return venda_id
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def buscar_por_id(self, venda_id):
        conexao = None
        cursor = None

        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """SELECT * FROM supermercado.vendas WHERE id = %s"""

            cursor.execute(sql,(venda_id,))
            vendas = cursor.fetchone()
            return vendas
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def excluir(self, venda_id):
        conexao =None
        cursor = None

        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """DELETE FROM vendas WHERE id = %s"""

            valores =(venda_id,)

            cursor.execute(sql,valores)

            quantidade = cursor.rowcount
            conexao.commit()
            return  quantidade
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def atualizar_total(self,venda_id, valor_total):
        conexao = None
        cursor = None

        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """UPDATE  vendas SET  valor_total = %s WHERE id =%s"""

            valores = (valor_total, venda_id,)

            cursor.execute(sql, valores)

            conexao.commit()
            quantidade = cursor.rowcount
            return  quantidade
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def atualizar_status(self,status,venda_id):
        conexao = None
        cursor = None

        try:
            conexao= criar_conexao()
            cursor = conexao.cursor()

            sql = """UPDATE vendas SET status = %s WHERE id = %s"""

            valores = (status, venda_id,)

            cursor.execute(sql,valores)

            conexao.commit()
            quantidade = cursor.rowcount
            return  quantidade
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def listar_todos(self):
        conexao = None
        cursor = None

        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql ="""SELECT * FROM supermercado.vendas"""

            cursor.execute(sql)
            vendas = cursor.fetchall()
            return  vendas
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()





