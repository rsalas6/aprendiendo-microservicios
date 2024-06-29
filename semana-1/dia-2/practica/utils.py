import hashlib

def verificar_hash(hash_calculado: str, cadena: str, tipo: str = 'md5') -> bool:
    """
    Verifica si el hash calculado de la cadena coincide con el hash dado.

    Args:
        hash_calculado (str): El hash previamente calculado y en formato hexadecimal.
        cadena (str): La cadena original.
        tipo (str): El tipo de hash utilizado ('md5', 'sha1', 'sha256'). Por defecto es 'md5'.

    Returns:
        bool: True si el hash calculado coincide con el hash dado, False en caso contrario.

    Raises:
        ValueError: Si el tipo de hash no es soportado.
    """
    # Verificar que el tipo de hash sea válido
    if tipo not in ['md5', 'sha1', 'sha256']:
        raise ValueError(f"Tipo de hash no soportado {tipo}. Use 'md5', 'sha1' o 'sha256'.")
    
    # Calcular el hash de la cadena original
    if tipo == 'md5':
        hash_object = hashlib.md5(cadena.encode())
    elif tipo == 'sha1':
        hash_object = hashlib.sha1(cadena.encode())
    elif tipo == 'sha256':
        hash_object = hashlib.sha256(cadena.encode())
    
    hash_cadena = hash_object.hexdigest()
    
    # Comparar el hash calculado con el hash dado
    return hash_cadena == hash_calculado