l1 = int(input('Insira o 1° Lado: '))
l2 = int(input('Insira o 2° Lado: '))
l3 = int(input('Insira o 3° Lado: '))

if ((l1 + l2 > l3) or (l1 + l3 > l2) or (l2 + l3 > l1)):
    print('Esses valores formam um triangulo, sendo ele: ')
    if (l1 == l2) and (l1 == l3):
        print('Eqüilátero')
    elif ((l1 == l2 != l3) or (l1 == l3 != l2) or (l2 == l3 !=l1)):
        print('isósceles')
    else:
        print('Escaleno')
else:
    print('Não é um triângulo')