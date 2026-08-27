from database.coneccao import criar_conexao
from models.produto import Produto

class ProdutoRepositorio:
    def cadastrar(self,produto):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        sql = """
        INSERT INTO produto (categoria, nome, preco, qtd_estoque)
        Values (%s,%s,%s,%s)
        """

        valores = (
            produto.categoria,
            produto.nome,
            produto.preco,
            produto.qtd_estoque
        )

        cursor.execute(sql,valores)

        conexao.commit()
        cursor.close()
        conexao.close()

    def listar_todos(self):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        sql = "SELECT ID,  categoria, nome, preco, qtd_estoque FROM produto"

        cursor.execute(sql)
        produtos = cursor.fetchall()

        cursor.close()
        conexao.close()

        return produtos