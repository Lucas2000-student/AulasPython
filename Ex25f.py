j = 1 
k = 0 
l = 0

print('Demonstrando os primeiros 20 números em Bergaschi')

for i in range(21):
    m = j + k + l
    print(f'{j}')
    print(f'{k}')
    print(f'{l}')
    print(f'{m}')
    j = m + k + l
    k = l + j + m
    l = j + k + m