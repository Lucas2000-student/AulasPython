p1 = int(input('Digite o 1° valor: '))
p2 = int(input('Digite o 2° valor: '))
p3 = int(input('Digite o 3° valor: '))

print('Após análise, o maior entre eles é: ')

if (p1 > p2 and p1 > p3):
    print(f'{p1}')
elif (p2 > p1 and p2 > p3):
    print(f'{p2}')
else:
    print(f'{p3}')