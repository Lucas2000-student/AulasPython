import cx_Oracle


# Cria String de conexão com informações do Host, Porta e SID
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='Orcl')


# Estabelece conexão com o BD
conn = cx_Oracle.connect(user='rm560179', password='fiap25', dsn=dsn)


# Abrir um cursor para executar comandos SQL
cursor = conn.cursor()


# Excluindo valores da tabela
cursor.execute("DELETE FROM TB_PYTHON_USER WHERE id=:valor1", valor1=3)
conn.commit()


print('Registro excluído com sucesso!')


# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()

