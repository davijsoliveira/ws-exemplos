import requests

def list_tickets():
    try:
        url = 'http://localhost:5000/list' 
        response = requests.get(url)

        if response.status_code == 200:
            tickets = response.json()
            print("Lista de tickets pagos:")
            for ticket in tickets:
                print(f"Número: {ticket['numero']}, Valor: {ticket['valor']}, Tempo: {ticket['tempo']}")
        else:
            print(f"Erro: {response.status_code} - {response.json().get('erro')}")

    except Exception as e:
        print(f"Erro na solicitação: {str(e)}")

if __name__ == '__main__':
    list_tickets()
