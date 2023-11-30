pipeline {
    agent any

    environment {
        FLASK_ENV = 'testing'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Puedes personalizar la construcción de tu imagen según tu docker-compose.yml
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Puedes personalizar la ejecución según tu docker-compose.yml
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Puedes ajustar esto según tus necesidades
                    sh 'docker-compose exec tu-servicio-python python -m venv venv'
                    sh 'docker-compose exec tu-servicio-python source venv/bin/activate'
                    sh 'docker-compose exec tu-servicio-python pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Puedes ajustar esto según tus necesidades
                    sh 'docker-compose exec tu-servicio-python python -m unittest discover tests'
                }
            }
        }
    }

    post {
        always {
            script {
                // Puedes ajustar esto según tus necesidades
                sh 'docker-compose down'
                echo 'Se han ejecutado las pruebas'
            }
        }
        success {
            echo 'Todo ha ido como esperábamos'
        }
        failure {
            echo 'Algo ha ido mal, revise su código'
        }
    }
}
