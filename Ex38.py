matriz = []

for l in range(0, 3, 1):
    matriz.append([])

for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        num = int(input('Digite um número: '))
        matriz[l].append(num)

fm = int(input('Defina um fator multiplicativo: '))

print('Matriz sem a multiplicação: ')
for l in range(0, 3, 1):
    print(matriz[l])

print('Matriz com a multipicação: ')
for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz[l][c] = matriz[l][c]*fm
    print(matriz[l])
