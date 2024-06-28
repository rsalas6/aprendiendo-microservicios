import hashlib

def convertir_a_hash(cadena: str, tipo: str = 'md5') -> str:
    """
    Convierte una cadena en un hash utilizando el algoritmo especificado (md5, sha1, sha256).

    Args:
        cadena (str): La cadena a ser hasheada.
        tipo (str): El tipo de hash a utilizar ('md5', 'sha1', 'sha256'). Por defecto es 'md5'.

    Returns:
        str: La representación hexadecimal del hash.

    Raises:
        ValueError: Si el tipo de hash no es soportado.
    """
    if tipo not in ['md5', 'sha1', 'sha256']:
        raise ValueError(f"Tipo de hash no soportado {tipo}. Use 'md5', 'sha1' o 'sha256'.")
    
    if tipo == 'md5':
        hash_object = hashlib.md5(cadena.encode())
    elif tipo == 'sha1':
        hash_object = hashlib.sha1(cadena.encode())
    elif tipo == 'sha256':
        hash_object = hashlib.sha256(cadena.encode())
    
    return hash_object.hexdigest()
