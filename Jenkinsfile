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
		
		stage('Install Docker Compose') {
		steps {
			script {
				sh 'sudo apt-get install docker-compose -y'  
			}
		}
}

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'docker-compose exec tu-servicio-python python -m venv venv'
                    sh 'docker-compose exec tu-servicio-python source venv/bin/activate'
                    sh 'docker-compose exec tu-servicio-python pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker-compose exec tu-servicio-python python -m unittest discover tests'
                }
            }
        }
    }

    post {
        always {
            script {
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
