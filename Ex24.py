i = 0
j = 1
k = 1

print('Demonstrando os os primeiros 30 valores de Fibonacci: ')

while (i <= 30):
    l = j + k
    print(f'{j}')
    print(f'{k}')
    print(f'{l}')
    j = l + k
    k = j + l
    i = i + 1

print('Programa finalizado!')
