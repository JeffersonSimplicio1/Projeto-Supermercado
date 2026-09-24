from database.coneccao import criar_conexao

class FuncionarioRepositorio:
    def cadastrar(self, funcionario):
        try:
            conexao =criar_conexao()
            cursor = conexao.cursor()

            sql = """INSERT INTO funcionario (nome, cargo, salario) VALUES (%s,%s,%s)"""

            valores = (
                funcionario.nome,
                funcionario.cargo,
                funcionario.salario
            )

            cursor.execute(sql,valores)
            funcionario_matricula = cursor.lastrowid

            conexao.commit()
            return funcionario_matricula
        finally:
            cursor.close()
            conexao.close()

    def buscar_por_id(self,funcionario_matricula):
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """SELECT * FROM supermercado.funcionario WHERE id = %s"""

            cursor.execute(sql,(funcionario_matricula, ))
            funcionarios = cursor.fetchone()
            return funcionarios
        finally:
            cursor.close()
            conexao.close()

    def buscar_por_nome(self, nome):
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """SELECT * FROM supermercado.funcionario WHERE nome = %s"""

            cursor.execute(sql,(nome, ))
            funcionarios = cursor.fetchall()
            return  funcionarios
        finally:
            cursor.close()
            conexao.close()

    def listar_todos(self):
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """SELECT * FROM funcionario"""

            cursor.execute(sql)
            funcionarios = cursor.fetchall()
            return funcionarios

        finally:
            cursor.close()
            conexao.close()

    def atualizar(self,funcionario_matricula, funcionario):
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql ="""UPDATE funcionario SET nome = %s, cargo = %s, salario = %s WHERE id = %s"""

            valores = (
                funcionario.nome,
                funcionario.cargo,
                funcionario.salario,
                funcionario_matricula
            )

            cursor.execute(sql, valores)
            quantidade = cursor.rowcount
            conexao.commit()
            return  quantidade > 0
        finally:
            cursor.close()
            conexao.close()

    def excluir_por_id(self, funcionario_matricula):
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            sql = """DELETE FROM supermercado.funcionario WHERE Id = %s"""

            valores = (funcionario_matricula, )

            cursor.execute(sql, valores)
            quantidade = cursor.rowcount
            conexao.commit()
            return  quantidade > 0
        finally:
            cursor.close()
            conexao.close()

    def excluir_por_nome(self, nome):
        try:
            conexao=criar_conexao()
            cursor = conexao.cursor()

            sql = """DELETE FROM supermercado.funcionario WHERE nome = %s"""

            valores = (nome, )

            cursor.execute(sql, valores)
            quantidade = cursor.rowcount
            conexao.commit()
            return quantidade

        finally:
            cursor.close()
            conexao.close()

