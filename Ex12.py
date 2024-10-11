p1 = int(input('Insira a base: ')) 
p2 = int(input('Insira a Altura: '))
area = p1 * p2
print(f'O terreno possui uma área de: {area}')

if (area > 100):
    print(f'Terreno grande')
else:
    print(f'Terreno pequeno')