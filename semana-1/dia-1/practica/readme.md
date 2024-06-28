# My Flask Microservice

Este proyecto es un microservicio Flask que proporciona un endpoint para convertir una cadena de texto en un hash utilizando diferentes algoritmos (md5, sha1, sha256).

## Requisitos

- Docker
- Task (opcional, para automatización de tareas)

## Comandos

### Construcción de Imágenes Docker

- Desarrollo: `task build-dev`
- Producción: `task build-prod`

### Ejecución de Contenedores Docker

- Desarrollo: `task run-dev`
- Producción: `task run-prod`

### Limpieza de Imágenes Docker

- `task clean`

### Despliegue

- `task push`

## Endpoint

### POST /hash

Convierte una cadena de texto en un hash.

- **URL**: `/hash`
- **Método**: `POST`
- **Datos**:
  - `string`: La cadena de texto.
  - `type`: Algoritmo (`md5`, `sha1`, `sha256`). Opcional, por defecto `md5`.

### Ejemplo de Solicitud `curl`

```sh
curl -X POST http://127.0.0.1:5000/hash -H "Content-Type: application/json" -d '{"string": "Hello, World!", "type": "md5"}'
```

## Estructura del Proyecto

```
practica/
  ├── .gitignore
  ├── __init__.py
  ├── app.py
  ├── Dockerfile.dev
  ├── Dockerfile.prod
  ├── readme.md
  ├── requirements.txt
  └── utils.py
```