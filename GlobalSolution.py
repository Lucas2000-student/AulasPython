n = 0
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
        tipo = input('Irá cadastrar um condomínio ou Apartamento: ')
        j = int(input('Digite a quantidade de membros para o cadastro: '))
        
        input()
    elif(n == 3):
        print('--- Sobre a Solar Connect ---')
        input()

print('Obrigado por Utilizar nossos serviços!')