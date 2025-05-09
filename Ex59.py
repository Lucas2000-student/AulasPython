import requests

nome = input('Digite o nome do domínio desejado: ')

url = f"https://brasilapi.com.br/api/registrobr/v1/{nome}"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    if (dados['status'] == 'AVAILABLE'):
        print('Pode usar e ser feliz!')
    else:
        print('infelizmente já tem dono...')
