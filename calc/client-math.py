import requests

# URL base do web service
base_url = 'http://localhost:5000'  # Certifique-se de ajustar a porta se necessário

# Dados para as operações matemáticas
dados = {'numero1': 10, 'numero2': 5}

# Testando a operação de adição
response = requests.post(f'{base_url}/adicao', json=dados)
print(f'Adição: {response.json()["resultado"]}')

# Testando a operação de subtração
response = requests.post(f'{base_url}/subtracao', json=dados)
print(f'Subtração: {response.json()["resultado"]}')

# Testando a operação de multiplicação
response = requests.post(f'{base_url}/multiplicacao', json=dados)
print(f'Multiplicação: {response.json()["resultado"]}')

# Testando a operação de divisão
response = requests.post(f'{base_url}/divisao', json=dados)
print(f'Divisão: {response.json()["resultado"]}')
