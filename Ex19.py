i = 1
po = 0
ne = 0
soma = 0

while (i <= 5):
    
    num = float(input('Insira um valor: '))

    if (i == 1):
        maior = num
        menor = num
    
    if (num >= 0):
        po = po + 1
    else:
        ne = ne + 1

    if (num > maior):
        maior = num
    if (num < menor):
        menor = num
    
    soma = soma + num
    i = i + 1

media = soma / 5

p1 = (po * 100) /5
p2 = (ne * 100) /5

print('Dado os valores é possivel dizer que:')
print(f'{maior} é o maior número, {menor} é o menor número')
print(f'A soma dos valores é {soma}, ea média deles é {media}')
print(f'E por fim, {p1}% é positivo e {p2}% é negativo')