p1 = float(input('insira o primeiro valor: '))
p2 = float(input('insira o segundo valor: '))
if (p1 > p2):
    print(f'{p1} É um valor maior que {p2}')
elif(p1 < p2):
    print(f'{p2} É um valor maior que {p1}')
else:
    print(f'Ambos são o mesmo valor')