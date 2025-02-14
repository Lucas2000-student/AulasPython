Clientes = []

while(True):
    print('\nBem vindo ao cadastro de pessoas!\n')
    nome = input('Digite seu nome: ')
    idade = int(input('sua idade: '))
    profissao = input('Profissão: ')
    salario = float(input('Salário: '))
    escolha = input('Quer cadastrar conta bancaria? (y/n): ')
    
    if(escolha == 'y'):
        banco = input('Nome do banco: ')
        agencia = int(input('Número da Agencia: '))
        numero = int(input('Número da conta: '))
        contas = {'banco': banco, 'agencia': agencia, 'numero': numero}
        cliente = {'nome': nome, 'idade': idade, 'profissao': profissao, 'salario': salario, 'conta': contas}
    
    else:
        cliente = {'nome': nome, 'idade': idade, 'profissao': profissao, 'salario': salario, 'conta': 'não informado.'}
    
    Clientes.append(cliente)
    print('Pessoa cadastrada!')
    choice = input('Deseja casdastrar mais alguém? (y/n): ')
    if(choice == 'n'):
        break
print('\nLista de pessoas cadastradas:\n')

for c in Clientes:
    if(c.get('conta') == 'não informado'):
        print(f'Nome: {c.get('nome')} | Idade: {c.get('idade')} | Profissão: {c.get('profissao')} | Salário: {c.get('salario')}')
    else:
        print(f'Nome: {c.get('nome')} | Idade: {c.get('idade')} | Profissão: {c.get('profissao')} | Salário: {c.get('salario')} | Conta: {c.get('banco')} | Agencia com Número: {c.get(agencia)} {c.get(numero)}')