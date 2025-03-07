matriz0 = []
matriz1 = []

for l in range(0, 3, 1):
    matriz0.append([])

for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        num = int(input('Digite um número: '))
        matriz0[l].append(num)

fm = int(input('Defina um fator multiplicativo: '))

print('Matriz sem a multiplicação: ')
for l in range(0, 3, 1):
    print(matriz0[l])

print('Matriz com a multipicação: ')
for l in range(0, 3, 1):
    for c in range(0, 4, 1):
        matriz1[l][c] = matriz0[l][c]*fm
    print(matriz1[l])