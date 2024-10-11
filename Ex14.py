p1 = float(input('insira a altura: '))
p2 = float(input('Insira peso: '))

m = p2 / (p1 * p1) 

if (m < 20):
    print(f'{m} Está abaixo do peso')
elif (20 <= m < 25):
    print(f'{m} Está no peso ideal')
else:
    print(f'{m:.2f} Está acima do peso')