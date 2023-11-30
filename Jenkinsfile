pipeline {
    agent any
	
	environment {
        PYTHON_VERSION = '3.8'
    }

    stages {
        stage('Install Python') {
            steps {
                script {
                    sh "command -v python${PYTHON_VERSION} || sudo apt-get install -y python${PYTHON_VERSION}"
                }
            }
        }
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

        stage('Run Tests') {
            steps {
                script {
                    sh "python${PYTHON_VERSION} -m venv venv"
                    sh 'source venv/bin/activate'

                    sh 'pip install -r app/requirements.txt'

                    sh "python${PYTHON_VERSION} -m unittest discover -s app -p 'test_*.py'"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado'
        }
    }
}
