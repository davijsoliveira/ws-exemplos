import requests

# URL base do web service
url = 'http://localhost:5000/payed' 

# Informações do ticket
ticket01 = {
    'numero': 4,
    'valor': 15,
    'tempo': '5h'
}

# Cadastrando ticket
response = requests.post(url, json=ticket01)

if response.status_code == 200:
    print("Ticket adicionado com sucesso!")
else:
    print(f"Erro: {response.status_code} - {response.json().get('erro')}")


