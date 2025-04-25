arquivo = open("D:\\baseDados.txt", "r")
conteudo = arquivo.read()
baseDados = conteudo.split(";")
listaCliente = []
listaProduto = []

for i in baseDados:
    if (i.startswith("C")):
        infoC = i.split(",")
        nome = infoC[0]
        idade = infoC[1]
        cidade = infoC[2]
        Cliente = {'nome': nome,'idade': idade, 'cidade': cidade}
        listaCliente.append(Cliente)
    else:
        infoP = i.split(",")
        nome = infoP[0]
        quant = infoP[1]
        preco = infoP[2]
        Produto = {'nome': nome,'quant': quant, 'preco': preco}
        listaProduto.append(Produto)

arquivo = open("D:\\clienteProduto.txt", "a")
for i in listaCliente:
    arquivo.write(f"Nome: {i.get('nome')[1:]}\nIdade: {i.get('idade')}\nCidade: {i.get('cidade')}\n\n")
for i in listaProduto:
    arquivo.write(f"Nome: {i.get('nome')[1:]}\nEstoque: {i.get('quant')}\nPreço: R${i.get('preco')}\n\n")