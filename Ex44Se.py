import cx_Oracle

# Cria String de conexão com informações do Host, Porta e SID
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')


# Estabelece conexão com o BD
conn = cx_Oracle.connect(user='rm560179', password='fiap25', dsn=dsn)


# Abrir um cursor para executar comandos SQL
cursor = conn.cursor()


# Executar uma consulta para ler o conteúdo de uma tabela
cursor.execute('SELECT * FROM TB_PYTHON_USER')


# Buscar todos os resultados da consulta
rows = cursor.fetchall()


# Exibir os resultados
for row in rows:
    print(row)
    print(f'Id: {row[0]}')
    print(f'Nome: {row[1]}')


# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
