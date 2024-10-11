print('Insira dois valores, sendo o 2° o maior\n')
v1 = int(input('1° Valor: '))
v2 = int(input('2° Valor: '))

while (v2 <= v1):
    print('O 2° tem que ser Maior')
    v2 = int(input('Digite novamente: '))

print(f'Treino concluído, {v2} é maior que {v1}')