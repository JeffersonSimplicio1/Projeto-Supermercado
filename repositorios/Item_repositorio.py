from database.coneccao import criar_conexao

class ItemRepositorio:
    def cadastrar(self,item):
        conexao = None
        cursor = None

        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """INSERT INTO itens_venda (venda_id, produto_id, quantidade,preco_unitario) VALUES (%s,%s,%s,%s)"""

            valores = (
                item.venda_id,
                item.produto_id,
                item.quantidade,
                item.preco_unitario
            )

            cursor.execute(sql, valores)
            item_id = cursor.lastrowid
            conexao.commit()
            return item_id

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def buscar_por_venda_id(self, venda_id):
        conexao = None
        cursor = None

        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """SELECT * FROM supermercado.itens_venda WHERE venda_id = %s"""

            cursor.execute(sql,(venda_id,))

            itens = cursor.fetchall()
            return itens
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

    def excluir(self, item_id):
        conexao = None
        cursor = None

        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """DELETE FROM itens_venda WHERE id = %s """

            valores =(item_id,)

            cursor.execute(sql,valores)

            quantidade =cursor.rowcount
            conexao.commit()
            return quantidade

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()



