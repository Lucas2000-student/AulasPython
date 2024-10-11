i = 0
j = 1
k = 1
l = 1

print('Demonstrando os primeiros 20 números em Bergaschi')

while (i <= 20):
    m = j + k + l
    print(f'{j}')
    print(f'{k}')
    print(f'{l}')
    print(f'{m}')
    j = m + k + l
    k = l + j + m
    l = j + k + m
    i = i + 1

print('Programa finalizado!')
