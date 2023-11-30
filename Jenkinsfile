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

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'python -m unittest discover tests'
                }
            }
        }
    }

    post {
        always {
            echo 'Se han ejecutado las pruebas'
        }
        success {
            echo 'Todo ha ido como esperábamos'
        }
        failure {
            echo 'Algo ha ido mal, revise su código'
        }
    }
}
