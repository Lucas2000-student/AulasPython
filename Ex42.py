arquivo = open("D:\\AlunosVestibular.txt", "r")
infos = arquivo.read()
listaInfos = infos.split(';')
listaAlunos = []

for i in listaInfos:
    Separador = i.split(',')
    nome = Separador[0]
    nota = Separador[1].lstrip()
    cidade = Separador[2].lstrip()
    Aluno = {'nome': nome,'nota': nota, 'cidade': cidade}
    listaAlunos.append(Aluno)

arquivo = open("D:\\AlunosAprovados.txt", "a")
for i in listaAlunos:
    arquivo.write(f"Nome: {i.get('nome')}\nNota: {i.get('nota')}\nCidade: {i.get('cidade')}\n\n")