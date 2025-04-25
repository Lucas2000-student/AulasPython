import cx_Oracle

# Cria String de conexão com informações do Host, Porta e SID
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='Orcl')


# Estabelece conexão com o BD
conn = cx_Oracle.connect(user='rm560179', password='fiap25', dsn=dsn)


# Abrir um cursor para executar comandos SQL
cursor = conn.cursor()


# Atualizando valores na tabela
cursor.execute("UPDATE TB_PYTHON_USER SET NOME=:valor1 WHERE ID=:valor2", valor1='Natan', valor2=1)
conn.commit()

print('Registro alterado com sucesso!')

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
