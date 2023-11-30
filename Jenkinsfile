pipeline {
    agent any

    stages {
		
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/Raul1992gt/Sprint_final.git']]])
            }
        }

        stage('Print Repository Contents') {
            steps {
                sh 'ls -la'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado'
        }
    }
}
