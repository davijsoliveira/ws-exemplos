import requests

# URL base do web service
url = 'http://localhost:5000/payed' 

# Dados para as operações matemáticas
ticket01 = {
    'numero': 4,
    'valor': 15,
    'tempo': '5h'
}
#ticket01 = {'numero': 1, 'valor': 19, 'tempo': 5}

# Cadastrando ticket
response = requests.post(url, json=ticket01)

if response.status_code == 200:
    print("Ticket adicionado com sucesso!")
else:
    print(f"Erro: {response.status_code} - {response.json().get('erro')}")

#response = requests.post(f'{url}/payed', json=ticket01)
#print(f'Resultado: {response.json()["mensagem"]}')


