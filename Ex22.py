i = 1
j = 1

print('Iniciando Tabuadas: ')

while (i <= 20):
    
    while (j <= 10):
        soma = i * j
        print(f'{i} x {j} = {soma}')
        j = j + 1
    
    k = int(input('Deseja continuar? digite 1 para SIM e 2 para NÃO: '))
    
    if (k == 1):
        i = i + 1
        j = 0
    else:
        i = 21
        print('Simulação encerrada')
    k = 0

print('Tabuadas concluídas!')