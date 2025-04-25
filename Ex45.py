import cx_Oracle

dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
conn = cx_Oracle.connect(user='rm560179', password='fiap25', dsn=dsn)
cursor = conn.cursor()

while(True):
    print('\nMercadão do TIO JOÃO\n')
    print("1 - Cadastrar Produto.\n2- Atualizar Produto.\n3- Excluir Produto.\n4- Listar Produtos.\n5- Listar Produto.\n6- Sair.")
    opc1 = int(input("Digite a opção desejada: "))
    
    if(opc1 == 1):
      
      nome = input("Digite o Nome do produto: ")
      preco = float(input("Digite o Preço: "))
      quant = int(input("A quantidade em estoque: "))
      cursor.execute("INSERT INTO TB_PYTHON_PRODUTO (ID, NOME, PRECO, QUANT) VALUES (:valor1, :valor2, :valor3, :valor4)", valor1=id, valor2=nome, valor3=preco, valor4=quant)
      conn.commit()
      print("Produto cadastrado!")
      id = id + 1
      input()

    elif(opc1 == 2):
       nome = input("Por favor insira o Nome do produto: ")
       preco = float(input('Digite o novo valor do Produto: '))
       quant = int(input("Digite a nova quantidade em estoque: "))
       cursor.execute("UPDATE TB_PYTHON_PRODUTO SET PRECO=:valor1 WHERE NOME=:valor2", valor1=preco, valor2=nome)
       cursor.execute("UPDATE TB_PYTHON_PRODUTO SET QUANT=:valor1 WHERE NOME=:valor2", valor1=quant, valor2=nome)
       conn.commit()
       print("Produto Atualizado!")
       input()

    elif(opc1 == 3):
       nome = input("Digite nome do produto a ser excluído: ")
       cursor.execute("DELETE FROM TB_PYTHON_PRODUTO WHERE NOME=:valor1", valor1=nome)
       conn.commit()
       print("produto excluído.")
       input()

    elif(opc1 == 4):
       print("Todos nossos Produtos: ")
       cursor.execute('SELECT * FROM TB_PYTHON_PRODUTO')
       rows = cursor.fetchall()
       for row in rows:
          print(f"ID: {row[0]} | Nome: {row[1]}\nPreço: R${row[2]}\nEm estoque: {row[3]}")
       input()

    elif(opc1 == 5):
       nome = input("Digite o nome do produto a ser exibido: ")
       cursor.execute("SELECT FROM TB_PYTHON_PRODUTO WHERE Nome=:valor1 ",valor1=nome)
       input()

    elif(opc1 == 6):
        break

cursor.close()
conn.close()