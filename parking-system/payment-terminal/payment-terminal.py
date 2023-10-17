import requests

# URL base do web service
url = 'http://localhost:5000/payed' 

# Informações do ticket
ticket = {
    'numero': 1,
    'valor': 12,
    'tempo': '4h'
}

# Cadastrando ticket
response = requests.post(url, json=ticket01)

if response.status_code == 200:
    print("Ticket adicionado com sucesso!")
else:
    print(f"Erro: {response.status_code} - {response.json().get('erro')}")


