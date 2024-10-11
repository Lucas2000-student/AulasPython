print('Iniciando Tabuadas: ')

for i in range(1,21):

    for j in range(1,11):
        soma = i * j
        print(f'{i} x {j} = {soma}')

    k = int(input('Deseja continuar? digite 1 para SIM e 2 para NÃO: '))
    
    if (k == 1):
        i = i + 1
        j = 0
    else:
        i = 21
        print('Simulação encerrada')

print('Tabuadas concluídas!')