from flask import Flask, request, jsonify

app = Flask(__name__)

# Tickets pagos
tickets = [{'numero': 2,'valor': 13,'tempo': '5h'}]

@app.route('/payed', methods=['POST'])
def pay():
    try:
        data = request.json
        numero = data.get('numero')
        valor = data.get('valor')
        tempo = data.get('tempo')
        ticket = {'numero': numero, 'valor': valor, 'tempo': tempo}
        tickets.append(ticket)
        print("O tamanho da lista é:", len(tickets))
        return jsonify({'mensagem': 'Ticket cadastro com sucesso'})
    
    except Exception as e:
        return jsonify({'erro': str(e)})

@app.route('/list', methods=['GET'])
def list():
    try:
        print("Conteúdo da lista de tickets:", tickets)
        return jsonify(tickets)
    except Exception as e:
        return jsonify({'erro': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
