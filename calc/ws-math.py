from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/adicao', methods=['POST'])
def adicao():
    try:
        data = request.json
        resultado = data['numero1'] + data['numero2']
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'erro': str(e)})

@app.route('/subtracao', methods=['POST'])
def subtracao():
    try:
        data = request.json
        resultado = data['numero1'] - data['numero2']
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'erro': str(e)})

@app.route('/multiplicacao', methods=['POST'])
def multiplicacao():
    try:
        data = request.json
        resultado = data['numero1'] * data['numero2']
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'erro': str(e)})

@app.route('/divisao', methods=['POST'])
def divisao():
    try:
        data = request.json
        resultado = data['numero1'] / data['numero2']
        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'erro': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
