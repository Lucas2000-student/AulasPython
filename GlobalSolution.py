condominio = []
predio =[]

n = 0
j = 0
h = 0
aptos = 0
casas = 0

while (n != 4):
    print('--- Bem vindo ao Solar Connect! ---\n')
    print('1 - Informações do Serviço.')
    print('2 - Realizar Cadastro.')
    print('3 - Vizualizar Pessoas cadastradas.')
    print('4 -  Sair.\n')
    n = int(input('Digite a opção desejada: '))
    print('\n')

    if(n == 1):
        print('--- Sobre a Solar Connect ---')
        print('Criamos está empresa com a ideia de ajudar prédios/condomínios a economizar na conta de energia e conhecer a energia solar.')
        print('Para isso, nós efetuamos um cálculo de custo energético total de todos os moradores por 1 mês.')
        print('Depois disso, efetuamos o levantamento de custo para a instalação de todos os equipamentos para suprir o gasto de energia.')
        print('Depois de tudo instalado, você e seus vizinhos poderam ver as informações de gastos e uso de energia.')
        print('Podendo efetuar a transferência de energia entre um ao outro.')
        input()
    elif(n == 2):
        print('--- Área de Cadastro ---')
        print('Qual o tipo de localidade?')
        print('1 - Prédio. \n2 - Condomínio.')
        j = int(input('Digite: '))
        if (j == 1):
            quant = int(input('Quantos Aptos: '))
            aptos = aptos + quant
            for i in range(quant):
                nome = input('Nome do dono: ')
                sobrenome = input('Sobrenome: ')
                apto = input('N° do Apto: ')
                moradores = input('N° de moradores: ')
                predio.append('Dono(a): ' + nome + ' ' + sobrenome + 'mora no apto ' + apto + ' em ' + moradores + 'pessoa(s)')
                print('\n')
            print('Cadastros concluídos!')
            input()
        elif(j == 2):
            quant = int(input('Quantas casas: '))
            casas = casas + quant
            for i in range(quant):
                nome = input('Nome do dono: ')
                sobrenome = input('Sobrenome: ')
                casa = (input('N° da casa: '))
                moradores = (input('N° de moradores: '))
                condominio.append('Dono(a): ' + nome + ' ' + sobrenome + 'mora na casa ' + casa + ' em ' + moradores + 'pessoa(s)')
                print('\n')
            print('Cadastros concluídos!')
            input()
    elif(n == 3):
        print('--- Área de visualização: ---')
        if (aptos > 0):
            print('Moradores do Prédio:')
            for u in range(aptos):
                print(predio(h))
                h = h + 1
            h = 0
        if (casas > 0):
            print('Moradores do Condomínio:')
            for u in range(casas):
                print(condominio(h))
                h = h + 1
            h = 0
        input()

print('Obrigado por Utilizar nossos serviços!')