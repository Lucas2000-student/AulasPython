lista_numeros = []


for i in range(10):
    num = int(input('Digite um valor: '))
    lista_numeros.append(num)


maior_num = lista_numeros[0]


for i in range(10):
    if (lista_numeros[i] > maior_num):
        maior_num = lista_numeros[i]


print(f'O maior número da lista é: {maior_num}')
