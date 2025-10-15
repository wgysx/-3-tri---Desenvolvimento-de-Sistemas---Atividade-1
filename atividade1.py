import requests

# URL da API
url = "https://jsonplaceholder.typicode.com/users"

# Fazendo o GET na API
response = requests.get(url)

# Verificando o status da resposta
if response.status_code == 200:
    # Convertendo a resposta para JSON
    users = response.json()
    
    # Exibindo os dados
    for user in users:
        print(f"Nome: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Endereço: {user['address']['street']}, {user['address']['city']}")
        print("-" * 40)
else:
    print(f"Erro ao acessar a API. Status code: {response.status_code}")
