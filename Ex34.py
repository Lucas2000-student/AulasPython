Alunos = []

while(True):
    print('\nBem Vindo ao cadastro de Alunos FIAP!\n')

    Nome = input('Digite seu nome: ')
    Ra = int(input('Digite seu RM: '))
    Curso = input('Digite seu Curso: ')

    TemConhecimento = input('Tem Conhecimento em alguma área? (Y/N): ').upper()
    Conhecimentos = []
    Linguagens = []

    if(TemConhecimento == 'Y'):
        while(True):
            Area = input('Digite a área de conhecimento (Ex: Backend): ')
            while(True):
                LingTec = input('Digite o nome da Linguagem/Tecnologia: ')
                mais = ('Conhece mais alguma? (Y/N): ').upper()
                if(mais == 'N'):
                    break
            mmais = input('Conhece mais alguma área?(Y/N)').upper()
            if(mmais == 'N'):
                break
            Linguagem = {'Ling': LingTec}
            Linguagens.append(Linguagem)
            Conhecimento = {'Area': Area, 'Linguagem': Linguagens}
            Conhecimentos.append(Conhecimento)
    
    Aluno = {'nome': Nome, 'RM': Ra, 'Curso': Curso, 'Conhecimento': Conhecimentos}
    Alunos.append(Aluno)

    mmmais = input('Deseja cadastrar mais um Aluno? (Y/N): ').upper()
    if(mmmais == 'N'):
        break

print('Lista de Alunos: ')

for a in Alunos:
    print(f'Aluno: {a.get('nome')} | Rm: {a.get('RM')} | Curso: {a.get('Curso')}')

    for ac in a.get('Conhecimentos'):
        print(f'Conhecimento na área de {ac.get('Area')}\n Linguagens/Tecnologias:')

        for al in ac.get('Linguagem'):
            print(f'{al.get('Ling')}, ')
