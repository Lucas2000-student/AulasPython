i = 0
l = 3
v = 2

print('Bem Vindo a sequência impar!')
n = int(input('Insira o valor de 1 a 100: '))

while(n <= 0) or (n > 100):
    if(n <= 0):
        print('ERRO! Valor negativo')
        n = int(input('Insira Novamente: '))
    else:
        print('ERRO! Valor acima de 100')
        n = int(input('Insira novamete: '))

while(i <= n):
    print(v)
    v = v + l
    l = l + 2
    i = i + 1