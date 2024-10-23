n = int(input('Insira o valor de 1 a 50: '))

while(n <= 0) or (n > 50):
    if(n <= 0):
        print('ERRO! Valor negativo')
        n = int(input('Insira Novamente: '))
    else:
        print('ERRO! Valor acima de 50')
        n = int(input('Insira novamete: '))

