j = 1, k = 0
print('Demonstrando os os primeiros 30 valores de Fibonacci: ')

for i in range(31):
    f = j + k
    print(f)
    j = k
    k = f