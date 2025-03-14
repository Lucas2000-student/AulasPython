Gabarito = [['A1','A2','A3','A4' ], ['B1','B2','B3','B4' ],['C1','C2','C3','C4' ],
            ['D1','D2','D3','D4' ],['E1','E2','E3','E4' ],['F1','F2','F3','F4' ],
            ['G1','G2','G3','G4' ],['H1','H2','H3','H4' ],['I1','I2','I3','I4' ],
            ['J1','J2','J3','J4' ],]
Bus = []
for i in range(10):
    Bus.append([])
    for j in range(4):
        Bus[i].append([j])
for i in range(10):
    for j in range(4):
        Bus[i][j] = Gabarito[i][j]

poltronas = 0

while(poltronas != 40):

    print('\nBem vindo ao Ônibus de Excursão Charlie B.Jr há Santos\n')

    for i in range (10):
        print(Gabarito[i])
    
    lugar = input('\nEscreva o local desejado: ').upper()
    for i in range (10):
        for j in range(4):
            if(Gabarito[i][j] == lugar):
                if(Gabarito[i][j] != 'X'):
                    Gabarito[i][j] = 'X'
                    nome = input('Digite seu nome: ')
                    Bus[i][j] = nome
                    print('Lugar Reservado!')
                    poltronas = poltronas + 1
                    break
                elif(Gabarito[i][j] == 'X'):
                    print('Lugar Já ocupado!')
                    break
                
    choice = input('Deseja Adicionar mais passageiros? (S/N)').upper()
    if (choice == 'N'):
        break

print('Aqui a Lista com os Nomes dos passageiros da viagem: ')

for i in range (10):
        print(Bus[i])
