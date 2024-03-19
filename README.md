# Microservicio de Métricas
Este microservicio proporciona endpoints para obtener métricas relacionadas con diferentes aspectos de un sistema. Utiliza FastAPI como framework para la creación de API RESTful y MongoDB para el almacenamiento de datos.

# Descripción del Servicio
El servicio cuenta con los siguientes endpoints:

* /metrics/sign-up: Obtiene métricas relacionadas con registros de usuarios.
* /metrics/country: Obtiene métricas relacionadas con la distribución geográfica de los usuarios.
* /metrics/sign-in: Obtiene métricas relacionadas con los inicios de sesión de los usuarios.
Cada endpoint devuelve un objeto JSON con las métricas correspondientes o un mensaje de error si las métricas no están disponibles.

# Instalación y Uso
* Clona este repositorio en tu máquina local.
* Instala las dependencias del proyecto ejecutando pip install -r requirements.txt.
* Ejecuta el microservicio utilizando el comando uvicorn app.main:app --reload.

