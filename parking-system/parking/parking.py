from flask import Flask, request, jsonify

app = Flask(__name__)

# Tickets pagos
tickets = []

@app.route('/payed', methods=['POST'])
def pay():
    try:
        data = request.json
        numero = data.get('numero')
        valor = data.get('valor')
        tempo = data.get('tempo')
        ticket = {'numero': numero, 'valor': valor, 'tempo': tempo}
        tickets.append(ticket)
        return jsonify({'mensagem': 'Ticket cadastro com sucesso'})
    
    except Exception as e:
        return jsonify({'erro': str(e)})

@app.route('/list', methods=['GET'])
def list():
    try:
        return jsonify(tickets)
    except Exception as e:
        return jsonify({'erro': str(e)})

@app.route('/check/<int:numero>', methods=['GET'])
def check_ticket(numero):
    try:
        for ticket in tickets:
            if ticket['numero'] == numero:
                return jsonify(ticket)
    except Exception as e:
        return jsonify({'erro': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
