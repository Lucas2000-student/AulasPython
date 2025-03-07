matriz = []

print('Criando sua própria Matriz! (Limite 10x10)\n')


while(True):
    l = int(input('Digite o valor de Linhas: '))
    if (l > 9 ):
        print('Erro! Valor maior que 10\n')
    else:
        break
while(True):
    c = int(input('Digite o valor de Colunas: '))
    if (c > 9 ):
        print('Erro! Valor maior que 10\n')
    else:
        break

for i in range (0, l, 1):
    matriz.append([])

print('\nMatriz criada! Agora vamos dar valores há ela!\n')

for i in range (0, l, 1):
    for j in range (0, c, 1):
        num = int(input('Digite um número: '))
        matriz[i].append(num)

print('\n Sua Matriz está pronta e com valores!\n')

for i in range (0, l, 1):
    print(matriz[i])

while(True):

    valor = int(input('\nDigite um dos valores da Lista: '))
    true = 0
    for i in range (0, l, 1):
        for j in range (0, c, 1):
            if(matriz[i][j] == valor):
                print(f'\nEste valor se encontra na linha {i} coluna {j}\n')
                true = 1
    if(true == 0):
        print('\nValor não encontrado na Matriz!\n')
    choice = input('Deseja Continuar? (Y/N): ').upper()
    if (choice == 'N'):
        break

