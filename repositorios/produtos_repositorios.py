from database.coneccao import criar_conexao

class ProdutoRepositorio:
    def cadastrar(self, produto):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        try:
            sql = """
                INSERT INTO produto (categoria, nome, preco, qtd_estoque)
                VALUES (%s,%s,%s,%s)
                """

            valores = (
                produto.categoria,
                produto.nome,
                produto.preco,
                produto.qtd_estoque
            )

            cursor.execute(sql, valores)
            produto_id = cursor.lastrowid

            conexao.commit()
            return produto_id

        finally:
            cursor.close()
            conexao.close()

    def listar_todos(self):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        try:

            sql = "SELECT ID,  categoria, nome, preco, qtd_estoque FROM produto"

            cursor.execute(sql)
            produtos = cursor.fetchall()
            return produtos
        finally:
            cursor.close()
            conexao.close()

    def atualizar(self, produto_id, produto):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        try:

            sql = """UPDATE produto SET categoria = %s, nome = %s, preco = %s, qtd_estoque = %s WHERE ID = %s"""

            valores = (
                produto.categoria,
                produto.nome,
                produto.preco,
                produto.qtd_estoque,
                produto_id
            )

            cursor.execute(sql, valores)
            quantidade = cursor.rowcount

            conexao.commit()
            return quantidade > 0
        finally:
            cursor.close()
            conexao.close()

    def excluir_por_id(self, produto_id):

        conexao = criar_conexao()
        cursor = conexao.cursor()
        try:

            sql = """DELETE FROM produto WHERE ID = %s"""

            valores = (
                produto_id,
            )

            cursor.execute(sql, valores)
            quantidade = cursor.rowcount

            conexao.commit()
            return quantidade > 0
        finally:
            cursor.close()
            conexao.close()

    def excluir_por_nome(self,nome):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        try:
            sql = """DELETE FROM produto WHERE nome = %s"""

            valores = (nome,)

            cursor.execute(sql, valores)

            quantidade = cursor.rowcount
            conexao.commit()
            return  quantidade

        finally:
            cursor.close()
            conexao.close()

    def buscar_id(self, produto_id):
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """SELECT  * FROM supermercado.produto WHERE id = %s"""

            cursor.execute(sql, (produto_id,))
            produtos = cursor.fetchone()
            return produtos
        finally:
            cursor.close()
            conexao.close()

    def buscar_por_nome(self, nome):
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = " SELECT * FROM supermercado.produto WHERE nome = %s"

            cursor.execute(sql, (nome,))
            produtos = cursor.fetchall()
            return produtos

        finally:
            cursor.close()
            conexao.close()