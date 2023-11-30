pipeline {
    agent any
	
	environment {
        PYTHON_VERSION = '3.8.12' // ajusta según tu entorno
        PYENV_ROOT = "/var/jenkins_home/tools/pyenv"
        PATH = "/var/jenkins_home/tools/pyenv/shims:/var/jenkins_home/tools/pyenv/bin:$PATH"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'apt-get update && apt-get install -y patch'
					sh 'sudo chmod 755 /var/lib/apt/lists/partial'
					sh 'sudo apt-get update'
                }
            }
        }

        stage('Install Python') {
            steps {
                script {
                    def pythonInstalled = sh(script: "command -v python${PYTHON_VERSION}", returnStatus: true) == 0

                    if (!pythonInstalled) {
                        echo "Instalando pyenv y Python ${PYTHON_VERSION}"
                        sh 'curl https://pyenv.run | bash'
                        sh "pyenv install ${PYTHON_VERSION}"
                        sh "pyenv global ${PYTHON_VERSION}"
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
