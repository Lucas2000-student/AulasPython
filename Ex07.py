p1 = float(input('Insira o valor da coxinha: '))
p2 = float(input('Insira o valor da Esfiha: '))
p3 = float(input('Insira o valor do pastel: '))
p4 = float(input('Insira o valor da coca: '))
p5 = float(input('Insira o valor da água: '))
soma = p1 + p2 + p3 + p4 + p5
print(f'O valor dos seus produtos é de {soma}')
pag = float(input('Quanto você irá pagar: '))
total = pag - soma
print(f'O seu troco será de {total}')

