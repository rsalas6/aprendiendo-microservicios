import os
from utils import convertir_a_hash
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'false').lower() in ['true', '1']

@app.route('/', methods=['POST'])
def generar_hash():
    data = request.json
    cadena = data.get('cadena')
    tipo_hash = data.get('type', 'md5')

    if not cadena:
        return jsonify({"error": "No se proporcionó ninguna cadena"}), 400
    
    try:
        hash = convertir_a_hash(cadena, tipo_hash)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({
        "cadena": cadena,
        "hash": hash,
        "tipo_hash": tipo_hash
    }), 200

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0')
