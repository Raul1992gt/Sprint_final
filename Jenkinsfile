pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/Raul1992gt/Sprint_final.git']]])
            }
        }
		
		stage('Show Repository Status') {
			steps {
				script {
					def repoStatus = sh(script: 'git status --porcelain', returnStdout: true).trim()
					echo "Estado del repositorio: ${repoStatus}"
				}
			}
		}

        stage('Print Repository Contents') {
            steps {
                sh 'ls -la'
            }
        }
		
		stage('Show Last Commit Info') {
			steps {
				script {
					def lastCommitInfo = sh(script: 'git log -1 --pretty=format:"%h - %an, %ar : %s"', returnStdout: true).trim()
					echo "Último commit: ${lastCommitInfo}"
				}
			}
		}

        stage('Count Commits') {
            steps {
                script {
                    def commitCount = sh(script: 'git rev-list --count HEAD', returnStdout: true).trim()
                    echo "Número de commits: ${commitCount}"
                }
            }
        }
		
		stage('List Branches') {
			steps {
				script {
					def branches = sh(script: 'git branch -a', returnStdout: true).trim()
					echo "Ramas disponibles: ${branches}"
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
