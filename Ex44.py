import cx_Oracle

dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
conn = cx_Oracle.connect(user='rm560179', password='fiap25', dsn=dsn)
cursor = conn.cursor()

id = 2
while(True):
    print("\n ALUNOS FIAP!!! \n")
    print("1 - Cadastrar Aluno.\n2- Atualizar Curso do aluno.\n3- Excluir Aluno.\n4- Listar Alunos.\n5- Listar Aluno.\n6- Sair.")
    opc1 = int(input("Digite a opção desejada: "))

    if(opc1 == 1):
      
      nome = input("Digite seu nome: ")
      rm = input("Seu RM: ")

      cursor.execute('SELECT * FROM TB_PYTHON_CURSOS')
      rows = cursor.fetchall()
      for row in rows:
        print(f'Id: {row[0]} | Nome: {row[1]}')
      curso = int(input("digite o ID do Curso: "))

      cursor.execute("INSERT INTO TB_PYTHON_ANULO (ID, NOME, RA, CURSO) VALUES (:valor1, :valor2, :valor3, :valor4)", valor1=id, valor2=nome, valor3=rm, valor4=curso)
      conn.commit()
      print("Aluno cadastrado!")
      id = id + 1
      input()

    elif(opc1 == 2):
       ra = input("Por favor insira o RM do usuário a ser alterado: ")
       cursor.execute('SELECT * FROM TB_PYTHON_CURSOS')
       rows = cursor.fetchall()
       for row in rows:
        print(f'Id: {row[0]} | Nome: {row[1]}')
       curso = int(input("digite o ID do Curso: "))
       cursor.execute("UPDATE TB_PYTHON_ANULO SET CURSO=:valor1 WHERE RA=:valor2", valor1=curso, valor2=ra)
       conn.commit()
       print("Curso do aluno Atualizado")
       input()

    elif(opc1 == 3):
       ra = input("Digite o RM do aluno a ser excluído: ")
       cursor.execute("DELETE FROM TB_PYTHON_ANULO WHERE RA=:valor1", valor1=ra)
       conn.commit()
       print("Aluno Excluído.")
       input()
    elif(opc1 == 4):
       print("Todos nossos Alunos: ")
       cursor.execute('SELECT * FROM TB_PYTHON_ANULO')
       rows = cursor.fetchall()
       for row in rows:
          print(f"ID: {row[0]}\nNome: {row[1]}\nRm: {row[2]}\nCurso: {row[3]}")
    elif(opc1 == 5):
       ra = input("Digite o RM do aluno a ser exibido: ")
       cursor.execute("SELECT FROM TB_PYTHON_ANULO WHERE RA=:valor1 ",valor1=ra)
       input()
    elif(opc1 == 6):
        break

cursor.close()
conn.close()