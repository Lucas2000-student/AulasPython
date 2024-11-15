m = 1
soma = 0

for i in range (10):
    
    n = int(input(f'Digite o {m}° Valor: '))
    while (n <=0):
        n = int(input('Por valor somente valores positivos: '))

    if (i == 0):
        numM = n
        numm = n
    if (numM < n):
        numM = n
    if (numm > n):
        numm = n
    
    soma = soma + n
    m = m + 1

media = soma % 10

print('Após valores digitados, as respóstas perspectivas são:')
print(f'Maior valor: {numM}')
print(f'Menor valor: {numm}')
print(f'Soma total: {soma}')
print(f'Média entre eles: {media}')