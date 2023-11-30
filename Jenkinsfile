pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Descargar el repositorio de GitHub
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/Raul1992gt/Sprint_final.git']]])
            }
        }

        stage('Print Repository Contents') {
            steps {
                // Imprimir el contenido del repositorio
                sh 'ls -la'
            }
        }

        // Agrega más etapas según tus necesidades

        stage('Run Tests') {
            steps {
                echo 'Ejecutar pruebas aquí...'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado'
        }
    }
}
