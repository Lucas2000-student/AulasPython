import requests

user = input('Digite seu Login de dev do Git: ')
url = f"https://api.github.com/users/{user}"
response = requests.get(url)
if response.status_code == 200:
    dados = response.json()
    print(f"Nome: {dados['name']}")
    print(f"Quant. Repositórios: {dados['public_repos']}")
    print(f"Seguidores: {dados['followers']}")
else:
    print("Usuário não encontrado")
    