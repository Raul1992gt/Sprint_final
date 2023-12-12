# Dockerized Flask API with PostgreSQL, Prometheus, Grafana, and Jenkins Integration

Este repositorio proporciona una configuración de Docker Compose para levantar contenedores de Python con Flask para una API, PostgreSQL para la base de datos, Prometheus para la supervisión, Grafana para la visualización y Jenkins para la integración continua.

## Requisitos previos
Asegúrate de tener Docker y Docker Compose instalados en tu máquina antes de comenzar.

## Estructura del repositorio

- `app/`: Contiene la aplicación Flask para la API con operaciones GET, POST, PUT, DELETE.
- `db/`: Directorio para los archivos de inicialización de PostgreSQL.
- `jenkins/`: Configuración y tareas de Jenkins.
- `prometheus/`: Configuración de Prometheus.
- `grafana/`: Configuración de Grafana.

## Uso

1. Clona este repositorio:

    ```bash
    git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/Raul1992gt/Sprint_final.git)
    cd tu-repositorio
    ```

2. Levanta los contenedores utilizando Docker Compose:

    ```bash
    docker-compose up -d
    ```

3. Accede a la API Flask en `http://localhost:5000`, Grafana en `http://localhost:3000`, Prometheus en `http://localhost:9090`, y Jenkins en `http://localhost:8080`.

## Integración con Jenkins

1. Configura una tarea de Jenkins para descargar automáticamente el repositorio después de un push.

2. Configura las acciones de la tarea para verificar la correcta ejecución del código y la API.

## Arquitectura AWS

La arquitectura en la nube AWS se puede implementar de la siguiente manera:

- **S3 (Amazon Simple Storage Service):** Utiliza S3 para almacenar archivos estáticos, registros, o cualquier otro recurso necesario para tu aplicación.

- **RDS PostgreSQL (Relational Database Service):** Utiliza RDS para la base de datos PostgreSQL, asegurando la escalabilidad y la administración simplificada.

Asegúrate de configurar las credenciales de AWS y ajustar la configuración de la aplicación y la base de datos según sea necesario.

## Contribuciones

Clases en Qualentum de cada una de las tecnologías mencionadas
https://stackoverflow.com/
https://docs.aws.amazon.com/
https://www.jenkins.io/doc/
https://grafana.com/docs/grafana/latest/
https://prometheus.io/
https://hub.docker.com/
...
