num = int(input('Insira um valor Positivo: '))
t1 = 1
t2 = 1

while(num <= 0):
    print('Valor POSITIVO')
    num = int(input('Tente novamente: '))
    t1 = t1 + 1

if (t1 >= 2):
    print(f'Ufa, {t1} depois você conseguiu')

print(f'Com o valor {num} escolhido, sua tabuada é: ')

while(t2 <= 10):
    r = num * t2
    print(f'{num} x {t2} = {r}')
    t2 = t2 + 1
