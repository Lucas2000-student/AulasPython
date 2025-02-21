produtos = []

while(True):

    print('\n Bem vindo ao cadastro de Produtos!\n')
    nome = input('Digite o nome do Produto: ')
    preco = float(input('Digite o valor do Produto: '))
    quant = int(input('Digite a quantidade do produto: '))

    temLoja = input('Este produto é comercialiazado em loja? (Y/N): ').upper()
    Lojas = []

    if(temLoja == 'S'):
        while(True):

            nomeLoja = input('Nome da Loja: ')
            cidade = input('cidade da loja: ')

            Loja = {'NomeLoja': nomeLoja, 'cidade': cidade}
            Lojas.append(Loja)

            MaisLojas = input('Tem mais alguma loja? (Y/N):').upper()

            if(MaisLojas == 'N'):
                break
    
    produto = {'Nome': nome, 'Preco': preco, 'Quantidade': quant, 'Lojas': Lojas}
    produtos.append(produto)

    MaisProduto = input('Deseja cadastrar mais produtos? (Y/N): ').upper()
    if(MaisProduto == 'N'):
        break

print('Lista de Produtos cadastrados: ')

for p in produtos:
    print(f'Nome: {p.get('Nome')} | Custa R${p.get('Preco')} | Tem {p.get('Quantidade')} em estoque.')

    for pd in p.get('Lojas'):
        print(f'Loja: {pd.get('NomeLoja')} | Na cidade: {pd.get('cidade')}')
        