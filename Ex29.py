lista_numeros = []


for i in range(10):
    num = int(input('Digite um número: '))
    lista_numeros.append(num)


for i in range(9, -1, -1):
    print(lista_numeros[i])
