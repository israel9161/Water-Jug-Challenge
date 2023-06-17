# Water-Jug-Challenge

# API de Operaciones de Baldes

Esta API permite realizar operaciones con baldes para llenar un balde X o Y hasta cierto valor Z, utilizando un balde Y como apoyo. Proporciona una interfaz para enviar los valores de X, Y y Z, y recibir los pasos realizados en formato JSON.

## Requisitos

- Python 3.7 o superior
- Bibliotecas Python: FastAPI, uvicorn, pydantic

## Instalación

Se recomienda usar un IDE dedicado a Python como PYCharm para probar la API

1. Clona este repositorio en tu máquina local.

git clone https://github.com/israel9161/Water-Jug-Challenge.git en main.py
Accede al directorio del repositorio.

Instala las dependencias usando pip.

pip install fastapi, pydantic, uvicorn

Uso
Inicia el servidor de la API con el siguiente comando:

uvicorn main:app --reload
Accede a la interfaz de la API en tu navegador web en la siguiente URL:

http://localhost:8000/docs
En la interfaz de la API, puedes realizar las siguientes operaciones:

Enviar una solicitud POST a /api/operaciones con los valores de X, Y y Z para obtener los pasos realizados en formato JSON.
Enviar una solicitud GET a /api/operaciones para obtener la lista de operaciones realizadas.

Ejemplo de Solicitud
Aquí hay un ejemplo de cómo enviar una solicitud POST utilizando cURL:

shell
Copy code
curl -X POST "http://localhost:8000/api/operaciones" -H "Content-Type: application/json" -d '{
    "X": 2,
    "Y": 10,
    "Z": 4
}'
La respuesta será un objeto JSON que contiene los pasos realizados para completar la operación.

Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún error, tienes una idea de mejora o deseas agregar una nueva característica, siéntete libre de abrir un issue o enviar un pull request.
 
