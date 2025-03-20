# Área de Funções e Váriaveis.

def EfetuarCadastroEstabelecimento(tipo):
        nome = input(f'Digite o nome do(a) {tipo}: ')
        endereco = input('Endereço (Sem número): ')
        num = int(input('Número: '))
        aber = input('Hora de Abertura: ')
        fech = input('Hora de Fechamento: ')
        Local = {'tipo': tipo, 'nome': nome, 'endereco': endereco, 'num': num, 'funcionamento': aber + '~' + fech}
        Locais.append(Local)

def ExibirLocal(tipo):
        print(f'Lista de todos os Lugares do tipo: {tipo}')
        for i in Locais:
                if(i.get('tipo') == tipo):
                        print(f'Nome: {i.get('nome')} \nEndereço: {i.get('endereco')} N° {i.get('num')} \nFuncionamento: {i.get('funcionamento')}')

def AdicionarOnibus(linha):
       nome = input(f'Digite o Nome da linha {linha}: ')
       inic = input('Nome do terminal de ínicio: ')
       end = input('Nome do terminal destino: ')
       temp = input('Intervalo entre onibûs: ')
       tarif = float(input('Valor da Passagem: '))
       bus = {'linha': linha, 'nome': nome, 'pTerminal': inic, 'fTerminal': end, 'intervalo': temp, 'tarifa': tarif}
       Onibus.append(bus)

def ExibirBus():
       for i in Onibus:
              print(f'Linha: {i.get('linha')}-{i.get('nome')}\n De {i.get('pTerminal')} até {i.get('fTerminal')}\n com intervalos de {i.get('intervalo')} | Tarifa: {i.get('tarifa')}')

Locais = []
Onibus = []

opc1 = 0 
opc2 = 0 
opc3 = 0 
opc4 = 0
opc5 = 0
tentativas = 0 

# Área do Programa.

while (opc1 != 5):
    print('\n====== TOTEM TRACKIA ======')                #Tela de Apresentação ao Usuário
    print('1 - Horário dos Trens.')                     #Pela falta de banco de dados, é necessario primeiro acessar o menu de "Manutenção"          
    print('2 - Pontos próximos.')                       #Caso tente usar qualquer uma das 3 primeiras opções sem configurar, terá uma tela de Crash
    print('3 - Onibus do terminal da estação.')
    print('4 - Área de Manutenção.')                    #Para que o Usuário não acesse essa Opção tem uma senha (1234) como proteção
    print('5 - Sair.\n')

    opc1 = int(input('Digite a opção desejada: '))

    if(opc1 == 1):
            print('Os trens das Linhas 8-9 Levam entre 4~10 minutos\n Aos domingos e feriados o tempo médio é 30minutos. ') 
            input()                                     #Quando houver Banco de dados aqui irá mostrar a posição do trem com detalhes
    elif(opc1 == 2):
            print('1 - Farmácia. \n'                    
                  '2 - Hospital. \n'
                  '3 - Hotel.\n'
                  '4 - Padaria.\n'
                  '5 - Shopping\n'
                  '6 - Posto Policial')
            opc2 = int(input('Digite a opção desejada: ')) #Aqui o Usuário poderá escolher o local que ele quer ver

            if(opc2 == 1):
                   tipo = 'farmacia'
                   print(f'todas ás farmácias por perto:\n')
                   ExibirLocal(tipo)
                   input()
            elif(opc2 == 2):
                   tipo = 'hospital'
                   print(f'todas os hospitais por perto:\n')
                   ExibirLocal(tipo)
                   input()
            elif(opc2 == 3):
                   tipo = 'hotel'
                   print(f'todas os hotéis por perto:\n')
                   ExibirLocal(tipo)
                   input()
            elif(opc2 == 4):
                   tipo = 'padaria'
                   print(f'todas ás padarias por perto:\n')
                   ExibirLocal(tipo)
                   input()
            elif(opc2 == 5):
                   tipo = 'shopping'
                   print(f'todas os shoppings por perto:\n')
                   ExibirLocal(tipo)
                   input()
            elif(opc2 == 6):
                   tipo = 'postopolicial'
                   print(f'todas os postos policiais por perto:\n')
                   ExibirLocal(tipo)
                   input()
    elif(opc1 == 3):
           print('Lista de Linhas de Onibûs da estação: ')
           ExibirBus()
           input()
    elif(opc1 == 4):
        tentativas = 0
        Password = int(input('Digite a senha: '))                   #Area de verificação da senha (1234)
        while(tentativas <= 1):
            if (Password == 1234):
                while(opc3 != 4):
                    print('\n====== Área Manutenção ======')          #Parte de configuração de todas as funcionalidades
                    print('1 - Configuração do Totem.\n'
                          '2 - Configuração de locais próximos.\n'
                          '3 - Configuração dos Ônibus.\n'
                          '4 - Sair.\n')

                    opc3 = int(input('digite a opção desejada: '))
                    if(opc3 == 1):
                        ToTemEst = input('Digite a estação que está esse totem: ')
                        ToTemLin = input('Digite a Linha desse Totem: ')
                        print('Configuração Concluída!')
                        input()
                    elif(opc3 ==  2):
                        print('1 - Farmácia. \n'                    
                              '2 - Hospital. \n'
                              '3 - Hotel.\n'
                              '4 - Padaria.\n'
                              '5 - Shopping\n'
                              '6 - Posto Policial')
                        opc4 = int(input('Digite o tipo do local para adicionar: '))
                        if(opc4 == 1):
                            tipo = 'farmacia'
                            EfetuarCadastroEstabelecimento(tipo)
                            print('Configuração Concluída!')
                            input()
                        elif(opc4 == 2):
                            tipo = 'hospital'
                            EfetuarCadastroEstabelecimento(tipo)
                            print('Configuração Concluída!')
                            input()
                        elif(opc4 == 3):
                            tipo = 'hotel'
                            EfetuarCadastroEstabelecimento(tipo)
                            print('Configuração Concluída!')
                            input()
                        elif(opc4 == 4):
                            tipo = 'padaria'
                            EfetuarCadastroEstabelecimento(tipo)
                            print('Configuração Concluída!')
                            input()
                        elif(opc4 == 5):
                            tipo = 'shopping'
                            EfetuarCadastroEstabelecimento(tipo)
                            print('Configuração Concluída!')
                            input()
                        elif(opc4 == 6):
                            tipo = 'postopolicial'
                            EfetuarCadastroEstabelecimento(tipo)
                            print('Configuração Concluída!')
                            input()
                          
                    elif(opc3 == 3):
                        linha = input('Digite o número da linha: ')
                        AdicionarOnibus(linha)
                        print('Configuração Concluída!')
                        input()
                          
                    elif(opc3 == 4):
                        print('Manutenções Concluidas!')
                        tentativas = tentativas + 3
            
            else:
                Password = int(input('Erro! Tente novamente: '))
                tentativas = tentativas + 1

print('Obrigado por utilizar o nosso Totem, esperamos ter te ajudado! ')

# Somente Cumprindo Entregável da Sprint

while(True):
    salvar = input('Gostaria de salvar alguma das suas listas? (S/N): ').upper()
    if(salvar == 'S'):
        print('Salvaremos as suas informaçoes das Lista de Onibûs e Estabelecimento.')
        print('1 - criar um novo arquivo. \n'
              '2 - Sobreescrever um arquivo.')
        opc5 = int(input('Digite a opção desejada.'))

        if(opc5 == 1):
            listas = list()
            arquivo = open("D:\\ArquivoListas.txt", "a")
            for i in Onibus:
                
                listas.append(f"Linha: {i.get('linha')}-{i.get('nome')}\n De {i.get('pTerminal')} até {i.get('fTerminal')}\n com intervalos de {i.get('intervalo')} | Tarifa: {i.get('tarifa')}")
                arquivo.writelines(listas)            
            for i in Locais:
                listas.append(f"Nome: {i.get('nome')} \nEndereço: {i.get('endereco')} N° {i.get('num')} \nFuncionamento: {i.get('funcionamento')}")
                arquivo.writelines(listas)
            print('Dados salvos com sucesso!')
            break
                  
        elif(opc5 == 2):
            listas = list()
            link = input('Digite corretamente o caminho para o arquivo: ')
            arquivo = open(link, "w")
            for i in Onibus:
                listas.append(f'Linha: {i.get('linha')}-{i.get('nome')}\n De {i.get('pTerminal')} até {i.get('fTerminal')}\n com intervalos de {i.get('intervalo')} | Tarifa: {i.get('tarifa')}')
                arquivo.writelines(listas)
            for i in Locais:
                listas.append(f"Nome: {i.get('nome')} \nEndereço: {i.get('endereco')} N° {i.get('num')} \nFuncionamento: {i.get('funcionamento')}")
                arquivo.writelines(listas)
            print('Dados salvos com sucesso!')
            break
    else:
          break