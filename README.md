# 4NOW Backend

Este proyecto es un backend de Django configurado para un entorno de desarrollo utilizando Docker y Docker Compose.

## Prerrequisitos

Antes de comenzar, asegúrate de tener instalados los siguientes software en tu máquina:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Python 3.9](https://www.python.org/)

## Instalación

Sigue estos pasos para configurar y ejecutar la aplicación en tu entorno local:

1. Clona este repositorio:

    ```bash
    git clone https://github.com/Dream-Team-HN/4NOW-BACKEND.git
    cd 4now-backend
    ```

2. Copia el archivo de variables de entorno:

    ```bash
    cp .env.example .env
    ```

3. Construye y levanta los contenedores usando Docker Compose:

    ```bash
    docker-compose up --build
    ```

4. Accede a la aplicación en tu navegador web:

    ```plaintext
    http://localhost:8000
    ```

## Instalación de Dependencias

Si necesitas instalar una nueva dependencia, sigue estos pasos:

1. Abre una shell en el contenedor de la aplicación backend:

    ```bash
    docker-compose exec backend sh
    ```

2. Instala la nueva dependencia utilizando `pip` dentro del contenedor. Por ejemplo, para instalar `requests`:

    ```bash
    pip install requests
    ```

3. Asegúrate de actualizar el archivo `requirements.txt`:

    ```bash
    pip freeze > requirements.txt
    ```

## Comandos Útiles

- Para detener los contenedores:

    ```bash
    Ctrl + C
    ```

- Para detener y eliminar todos los contenedores, redes y volúmenes creados por Docker Compose:

    ```bash
    docker-compose down
    ```