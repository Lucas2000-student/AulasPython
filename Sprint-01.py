i = 0
while (i <= 1): #Crianção do Loop de repetição
    
    print('Bem Vindo!') #Apresentação das escolhas ao usuário
    print('1 - Horário dos trens.')
    print('2 - Pontos próximos.')
    print('3 - Sobre a estação.')
    print('4 - Sair.')
    n = int(input('Por favor digite a opção desejada: '))

    while (n <= 0) or (n > 4): #Caso o usuário digite algo incorreto
        print('ERRO! Caracter inválido.')
        n = int(input('Digite novamente: '))
       
    if (n == 1): #Futuramente essa opção irá Mostrar em tempo real o próximo trem até a estação.
        print('Os trens normalmente variam entre 6min ~ 12min.')
        print('Domingos e feriados são 32min.')

    elif (n ==2): #Futuramente terá integração com o mapa do entorno da estação.
        print('O que deseja encontrar?')
        print('1 - Shopping.')
        print('2 - Cafés e lanchonetes.')
        print('3 - Mercado.')
        o = int(input('Digite a opção: '))

        while (o <= 0) or (o > 3): #Caso o usuário digite algo incorreto
            print('ERRO! Caracter inválido.')
            o = int(input('Digite novamente: '))

        if (o == 1):
            #Exemplo ilustrativo.
            print('O Shopping sonhos e esperanças está a 700metros na rua papel,40')
        elif (o == 2):
            #Exemplos ilustrativos.
            print('Padaria pão bom há 350metros na rua dos sonhos,32')
            print('Mc Lanche tristes a 480metros na rua rei dos hamburgueres, 3')
        else:
            #Exemplo ilustrativo.
            print('CarreFive a 600metros na rua mercados,121')
    
    elif (n == 3): #Integração com o mapa interno da estação para informações internas.
            #Exemplos ilustrativos.
            print('Máquina de compra de bilhetes ao lado das catracas de entrada para a plataforna')
            print('Banheiros estão localizados no fim das plataformas, e ao lado da área de segurança.')

    else: #Fim do Loop.
         print('Obrigado por utilizar o nosso totem, espero ter ajudado!') 
         i = 2
         
    