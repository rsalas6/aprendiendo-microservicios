from fastapi import FastAPI, Request, status, HTTPException
from pydantic import BaseModel
from utils import verificar_hash

app = FastAPI()

class HashRequest(BaseModel):
    hash: str
    cadena: str
    tipo_hash: str = 'md5'

@app.post("/")
async def verify_hash(request: Request, body: HashRequest):   
    # Verificar que los datos necesarios estén presentes
    if not body.hash or not body.cadena:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Faltan datos requeridos")
    
    try:
        # Verificar el hash utilizando la función verificar_hash
        es_valido = verificar_hash(body.hash, body.cadena, body.tipo_hash)
        

    except ValueError as e:
        # Capturar excepción de verificar_hash y lanzar un HTTPException con detalle de error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    return {
        **body.dict(),
        "es_valido": es_valido
    }
