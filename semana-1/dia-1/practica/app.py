import os
import utils
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'false').lower() in ['true', '1']

@app.route('/', methods=['POST'])
def generar_hash():
    data = request.json
    cadena_a_hashear = data.get('string')
    tipo_hash = data.get('type', 'md5')

    if not cadena_a_hashear:
        return jsonify({"error": "No se proporcionó ninguna cadena"}), 400
    
    try:
        resultado_hash = utils.convertir_a_hash(cadena_a_hashear, tipo_hash)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"mensaje": "Hash generado", "resultado": resultado_hash, "tipo": tipo_hash}), 200

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0')
