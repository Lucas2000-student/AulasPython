x = int(input('Insira um valor positivo: '))

while (x <= 0):
    print('ERRO, Valor negativo detectado!')
    x = int(input('Digite novamente: '))

a = int(input('Insira o menor valor para tabuada: '))

b = int(input('Insira um valor superior ao anterior: '))
while (b <= a):
    print('ERRO, Valor escolhido menor que o anterior')
    b = int(input('Digite novamente: '))

print('Apos preset, aqui está seu resultado: ')



while(b > a):

    soma = x * b

    print(f'{x} x {b} = {soma}')

    b = b - 1
    