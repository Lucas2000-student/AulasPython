                      # Todas as ArrayList que esse programa usa com váriaveis de apoio.

Farmacia = []         #Fa.
Hospital = []         #Hp.
Hotel = []            #Ho.
Padaria = []          #Pa.
Shopping = []         #Spp.
PostoPolicial = []    #Pp.
Onibus = []           #Bus.

                      # Variaveis de apoio ao laço de repetição While.
i = 0 
j = 0 
k = 0 
l = 0

h = 0                 # "h" de "Help" Ele ajuda na listagem de repetição do laço For.
tentativas = 0        # Variavel de bloqueio de acesso ao menu de manutenção.
                      # Variaveis de apoio antes ditas.
Fa = 0
Hp = 0
Ho = 0
Pa = 0
Spp = 0
Pp = 0
Bus = 0

while (i != 6):
    print('====== TOTEM TRACKIA ======')                #Tela de Apresentação ao Usuário
    print('1 - Horário dos Trens.')                     #Pela falta de banco de dados, é necessario primeiro acessar o menu de "Manutenção"
    print('2 - Sobre a Estação.')                       #Caso tente usar qualquer uma das 4 primeiras opções sem configurar, terá uma tela de Crash
    print('3 - Pontos próximos.')
    print('4 - Onibus do terminal da estação.')
    print('5 - Área de Manutenção.')                    #Para que o Usuário não acesse essa Opção tem uma senha (1234) como proteção
    print('6 - Sair.')

    i = int(input('Digite a opção desejada: '))

    if(i == 1):
        print('Os trens da Linha ' + linha + ' costumam levar em média 4 há 10 minutos') #Quando houver Banco de dados aqui irá mostrar a posição do trem com detalhes
        print('Porém em domingos e feriados tem tempo médio de 30minutos.')
        input()                                                                          
    elif(i == 2):
        print('Tarifa comum: R$' + Tarifa)                                               #E aqui Mostrará lugares internos da estação como, banheiros
        print('Tarifa de estudante: R$' + TarifaEstudante)
        print('Ha estação ' + estacao + ' fica na rua ' + rua)
    elif(i == 3):
        print('==== Lista de Locais Próximos ======')   #Aqui o Usuário poderá escolher o local que ele quer ver
        print('1 - Farmácia.')
        print('2 - Hospital.')
        print('3 - Hotel.')
        print('4 - Padaria.')
        print('5 - Shopping')
        print('6 - Posto Policial')
        l = int(input('Digite a opção desejada'))
        if(l == 1):
            print('==== Lista de Farmácias Proximas ======')
            for u in range(Fa-1):
                print(Farmacia(h))
                h = h + 1
            h = 0
            input()

        elif(l == 2):
            print('==== Lista de Hospitais Proximos ======')
            for u in range(Hp-1):
                print(Hospital(h))
                h = h + 1
            h = 0
            input()

        elif(l == 3):
            print('==== Lista de Hotéis Proximos ======')
            for u in range(Ho-1):
                print(Hotel(h))
                h = h + 1
            h = 0
            input()

        elif(l == 4):
            print('==== Lista de Padarias Proximos ======')
            for u in range(Pa-1):
                print(Padaria(h))
                h = h + 1
            h = 0
            input()

        elif(l == 5):
            print('==== Lista de Shoppings Proximos ======')
            for u in range(Spp-1):
                print(Shopping(h))
                h = h + 1
            h = 0
            input()

        elif(l == 6):
            print('==== Lista de Postos Policiais Proximos ======')
            for u in range(Pp-1):
                print(PostoPolicial(h))
                h = h + 1
            h = 0
            input()

    elif(i == 4):
        print('Onibus Listados do terminal: ')
        for u in range(Bus-1):
                print(Onibus(h))
                h = h + 1
                h = 0
        input()

    elif(i == 5):
        Password = int(input('Digite a senha: '))                   #Area de verificação da senha (1234)
        while(tentativas <= 1):
            if (Password == 1234):
                while(j != 5):
                    print('====== Área Manutenção ======')          #Parte de configuração de todas as funcionalidades
                    print('1 - Configuração do Totem.')
                    print('2 - Configuração de locais próximos.')
                    print('3 - Alteração no valor das tarifas.')
                    print('4 - Confiuração dos Ônibus.')
                    print('5 - Sair.')

                    j = int(input('Digite a opção desejada: '))

                    if (j == 1):
                        estacao = int(input('Nome da estação: '))
                        rua = int(input('Rua da estação: '))
                        linha = int(input('Linha da estação: '))
                        print('Informações do Totem atualizadas!')
                        input()

                    elif(j == 2):
                        while(k != 7):
                            print('====== Locais próximos ====')
                            print('1 - Farmácia.')
                            print('2 - Hospital.')
                            print('3 - Hotel.')
                            print('4 - Padaria.')
                            print('5 - Shopping.')
                            print('6 - Posto Policial.')
                            print('7 - Sair.')

                            k = int(input('Digite a opção desejada: '))

                            if(k == 1):
                                print('====== Farmácia ======')
                                Pnome = int(input('Nome: '))
                                Paber = int(input('Horá de abertura'))
                                Pfec = int(input('Horário de fechamento: '))
                                Pendereco = int(input('Nome da rua: '))
                                Pnumero = int(input('Número: '))
                                Pdist = int(input('Distância (em metros): '))

                                Farmacia.append('Farmácia ' + Pnome + ' fica há' + Pdist + 'm na rua ' + Pendereco + ' N°' + Pnumero + '.\n Aberta das: ' + Paber + ' ~ ' + Pfec)
                                print('Farmácia cadastrada! ')
                                Fa = Fa + 1
                                input()

                            elif(k == 2):
                                print('====== Hospital ======')
                                Pnome = int(input('Nome: '))
                                Pendereco = int(input('Nome da rua: '))
                                Pnumero = int(input('Número: '))
                                Pdist = int(input('Distância (em metros): '))

                                Hospital.append('Hospital ' + Pnome + ' fica há' + Pdist + 'm na rua ' + Pendereco + ' N°' + Pnumero + '.\n Aberto 24horas.')
                                print('Hospital cadastrado! ')
                                Hp = Hp + 1
                                input()

                            elif(k == 3):
                                print('====== Hotel ======')
                                Pnome = int(input('Nome: '))
                                Paber = int(input('Horá de abertura'))
                                Pfec = int(input('Horário de fechamento: '))
                                Pendereco = int(input('Nome da rua: '))
                                Pnumero = int(input('Número: '))
                                Pdist = int(input('Distância (em metros): '))

                                Hotel.append('Hotel ' + Pnome + ' fica há' + Pdist + 'm na rua ' + Pendereco + ' N°' + Pnumero + '\n Aberto das: ' + Paber + ' ~ ' + Pfec)
                                print('Hotel cadastrado! ')
                                Ho = Ho + 1
                                input()
    
                            elif(k == 4):
                                print('====== Padaria ======')
                                Pnome = int(input('Nome: '))
                                Paber = int(input('Horá de abertura'))
                                Pfec = int(input('Horário de fechamento: '))
                                Pendereco = int(input('Nome da rua: '))
                                Pnumero = int(input('Número: '))
                                Pdist = int(input('Distância (em metros): '))

                                Padaria.append('Padaria ' + Pnome + ' fica há' + Pdist + 'm na rua ' + Pendereco + ' N°' + Pnumero + '\n Aberta das: ' + Paber + ' ~ ' + Pfec)
                                print('Padaria cadastrada! ')
                                Pa = Pa + 1
                                input()
    
                            elif(k == 5):
                                Spp = 0
                                print('====== Shopping ======')
                                Pnome = int(input('Nome: '))
                                Paber = int(input('Horá de abertura'))
                                Pfec = int(input('Horário de fechamento: '))
                                Pendereco = int(input('Nome da rua: '))
                                Pnumero = int(input('Número: '))
                                Pdist = int(input('Distância (em metros): '))

                                Shopping.append('Shopping ' + Pnome + ' fica há' + Pdist + 'm na rua ' + Pendereco + ' N°' + Pnumero + '\n Aberto das: ' + Paber + ' ~ ' + Pfec)
                                print('Shopping cadastrado! ')
                                Spp = Spp + 1
                                input()

                            elif(k == 6):
                                Pp = 0
                                print('====== Posto Policial ======')
                                Ptipo = int(input('Tipo de Posto: '))
                                Pnome = int(input('Nome: '))
                                Paber = int(input('Horá de abertura'))
                                Pfec = int(input('Horário de fechamento: '))
                                Pendereco = int(input('Nome da rua: '))
                                Pnumero = int(input('Número: '))
                                Pdist = int(input('Distância (em metros): '))

                                PostoPolicial.append(Ptipo + ' ' + Pnome + ' fica há' + Pdist + 'm na rua ' + Pendereco + ' N°' + Pnumero + '\n Aberto das: ' + Paber + ' ~ ' + Pfec)
                                print('Posto Policial cadastrado! ')
                                Pp = Pp + 1
                                input()

                    elif(j == 3):
                        Tarifa = float(input('Digite o novo valor da tarifa: '))
                        TarifaEstudante = Tarifa % 2
                        print('Tarifa atualizada!')
                        input()
                    
                    elif(j == 4):
                        print('====== Configuração Onibus ======')
                        Olinha = int(input('Numero da Linha: '))
                        Onome = int(input('Nome da Linha: '))
                        Otarifa = float(input('Tarifa da Linha: '))
                        Oquantidade = int(input('Quantidade de Onibus da frota: '))
                        Ointervalo = int(input('Intervalo entre onibus: '))
                        Oinic = int(input('Inicio do horário da frota: '))
                        Ofim = int(input('Fim do horário da frota: '))

                        Onibus.append('Onibus da linha ' + Olinha + ' ' + Onome + ' com a tarifa de R$' + Otarifa + ' faz o trajeto dás ' + Oinic + ' ~ ' + Ofim + ' com um intervalo de ' + Ointervalo)
                        print('Linha de Onibus cadastrada!')
                        Bus = Bus + 1
                        input()

                    elif(j == 5):
                        print('Manutenção finalizada')
                        tentativas = 3
                        input()
            else:
                Password = int(input('Erro! Tente novamente: '))
                tentativas = tentativas + 1
        
    tentativas = 0
    
    print('Obrigado por utilizar o nosso Totem, esperamos ter te ajudado! ')