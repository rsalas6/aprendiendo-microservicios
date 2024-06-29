# My FastAPI Microservice

Este proyecto es un microservicio FastAPI que proporciona un endpoint para verificar si un hash corresponde a una cadena de texto utilizando diferentes algoritmos (md5, sha1, sha256).

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

### POST /

Verifica si un hash corresponde a una cadena de texto.

- **URL**: `/`
- **Método**: `POST`
- **Datos**:
  - `hash`: El hash a verificar.
  - `cadena`: La cadena de texto original.
  - `tipo_hash`: Algoritmo (`md5`, `sha1`, `sha256`). Opcional, por defecto `md5`.

### Ejemplo de Solicitud `curl`

```sh
curl -X POST http://127.0.0.1:5001/ -H "Content-Type: application/json" -d '{"hash": "5d41402abc4b2a76b9719d911017c592", "cadena": "hello", "tipo_hash": "md5"}'
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
  ├── taskfile.yml
  └── utils.py
```

### Descripción de los Archivos

- **.gitignore**: Lista de archivos y directorios a ignorar por git.
- **__init__.py**: Archivo necesario para tratar el directorio como un módulo de Python.
- **app.py**: Contiene la lógica principal de la aplicación FastAPI.
- **Dockerfile.dev**: Dockerfile para el entorno de desarrollo.
- **Dockerfile.prod**: Dockerfile para el entorno de producción.
- **readme.md**: Este archivo.
- **requirements.txt**: Lista de dependencias de Python necesarias para el proyecto.
- **taskfile.yml**: Archivo de configuración de Task para automatización de tareas.
- **utils.py**: Funciones utilitarias usadas por `app.py`.