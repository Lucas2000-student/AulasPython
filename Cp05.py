Produtos = []

print('Venha cadastrar 5 produtos!')
i = 1

while(i <= 5):
    nome = input(f'Digite o nome do {i}° produto: ')
    preco = float(input('Digite o valor do produto: '))
    quant = int(input('Digite a quantidade de produtos'))
    total = preco * quant
    Produto = {'nome': nome, 'preco':preco, 'quant': quant, 'total': total}
    Produtos.append(Produto)
    
    print(f'{i}° Produto adicionado!')
    i = i + 1
    input()

print('Lista dos produtos:\n')
for j in Produtos:
    print(f'Nome: {j.get('nome')}\nValor total: {j.get('total')}\n')