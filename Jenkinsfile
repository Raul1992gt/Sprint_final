pipeline {
    agent any
	
	environment {
        PYTHON_VERSION = '3.8'
    }

    stages {
        stage('Install Python') {
            steps {
                script {
                    // Verifica si Python está instalado
                    def pythonInstalled = sh(script: "command -v python${PYTHON_VERSION}", returnStatus: true) == 0

                    // Si no está instalado, instala Python localmente en el directorio de trabajo del pipeline
                    if (!pythonInstalled) {
                        echo "Instalando Python ${PYTHON_VERSION}"
                        sh "curl -O https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz"
                        sh "tar -xvf Python-${PYTHON_VERSION}.tgz"
                        sh "cd Python-${PYTHON_VERSION} && ./configure --prefix=/var/jenkins_home/tools/python && make && make install"
                        sh "export PATH=/var/jenkins_home/tools/python/bin:$PATH"
                    }
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
