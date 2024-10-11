j = 1
k = 2

print('Bem Vindo a sequência impar!')
n = int(input('Insira o valor de 1 a 50: '))

while(n <= 0) or (n > 50):
    if(n <= 0):
        print('ERRO! Valor negativo')
        n = int(input('Insira Novamente: '))
    else:
        print('ERRO! Valor acima de 50')
        n = int(input('Insira novamete: '))

for i in range(n+1):
    print(f'{j}/{k}')
    j = j + 1
    k = k + 1
    i = i + 1