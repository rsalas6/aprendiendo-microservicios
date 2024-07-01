# CLI para la Interconexión de Microservicios

Este proyecto es un CLI (Command Line Interface) que permite enviar una cadena de texto a un servicio Flask para generar un hash y luego verificar dicho hash utilizando un servicio FastAPI. Este CLI demuestra cómo los microservicios pueden interconectarse y comunicarse entre sí.

## Requisitos

- Docker

## Comandos

### Construcción de Imágenes Docker

- Construcción del CLI: `docker build -t cli_intermediary .`

### Ejecución de Contenedores Docker

- Ejecución del CLI: `docker run --rm --network host cli_intermediary --cadena "hello" --tipo "md5"`

## Ejemplo de Ejecución

Para ejecutar el CLI y hacer una solicitud a los servicios Flask y FastAPI que están corriendo en tu máquina local, usa el siguiente comando:

```sh
docker run --rm --network host cli_intermediary --cadena "hello" --tipo "md5"
```

## Funcionamiento del CLI

El CLI toma dos argumentos:

- `--cadena`: La cadena de texto para enviar a los servicios Flask y FastAPI.
- `--tipo`: El tipo de hash a generar (`md5`, `sha1`, `sha256`). Opcional, por defecto `md5`.

El proceso es el siguiente:
1. Genera el hash de la cadena de texto utilizando el algoritmo especificado.
2. Envía la cadena de texto al servicio Flask para generar el hash.
3. Verifica el hash generado enviándolo al servicio FastAPI.
4. Imprime las respuestas obtenidas de ambos servicios.

## Estructura del Proyecto

```
practica/
  ├── cli.py
  ├── docker-compose.yml
  ├── Dockerfile
  ├── readme.md
  ├── requirements.txt
  ├── teoria.md
```

### Descripción de los Archivos

- **cli.py**: Contiene la lógica principal del CLI.
- **docker-compose.yml**: Archivo de configuración para Docker Compose.
- **Dockerfile**: Define la imagen Docker para el CLI.
- **readme.md**: Este archivo.
- **requirements.txt**: Lista de dependencias de Python necesarias para el proyecto.
- **teoria.md**: Documentación teórica sobre el proyecto.