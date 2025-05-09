import requests

real = float(input('Digite o valor em real: '))

print('Opções de conversão: ')
print('1° Dólar \n2° Euro\n3° Bitcoin')
opc = int(input('Digite a opção desejada: '))

if(opc == 1):
    url = f"https://economia.awesomeapi.com.br/json/last/USD-BRL"
    response = requests.get(url)
    dados = response.json()
    variacao = float((dados['USDBRL']['ask']))
    total = real / variacao
    print(f'Em dolar será = {total:.2f}')
elif(opc == 2):
    url = f"https://economia.awesomeapi.com.br/json/last/EUR-BRL"
    response = requests.get(url)
    dados = response.json()
    variacao = float(dados['EURBRL']['ask'])
    total = real / variacao
    print(f'Em Euro será = {total:.2f}')
elif(opc == 3):
    url = f"https://economia.awesomeapi.com.br/json/last/BTC-BRL"
    response = requests.get(url)
    dados = response.json()
    variacao = float(dados['BTCBRL']['ask'])
    total = real / variacao
    print(f'Em Euro será = {total:.2f}')