import hashlib
import requests
import click

@click.command()
@click.option('--cadena', required=True, help='La cadena de texto para enviar al servicio Flask y FastAPI.')
@click.option('--tipo', default='md5', help='El tipo de hash (md5, sha1, sha256).')
def process_request(cadena, tipo):
    # Generar el hash de la cadena usando el tipo especificado
    if tipo not in ['md5', 'sha1', 'sha256']:
        print(f"Tipo de hash no soportado: {tipo}. Use 'md5', 'sha1' o 'sha256'.")
        return

    # Forward request to Flask service
    flask_data = {
        "cadena": cadena,
        "tipo_hash": tipo
    }
    flask_response = requests.post('http://192.168.1.95:5000/', json=flask_data)
    flask_result = flask_response.json()
    print("# Flask Response:", flask_result)

    if flask_response.status_code == 200:
        fastapi_response = requests.post('http://192.168.1.95:5001/', json=flask_result)
        fastapi_result = fastapi_response.json()
        print("# FastAPI Response:", fastapi_result)

if __name__ == '__main__':
    process_request()
