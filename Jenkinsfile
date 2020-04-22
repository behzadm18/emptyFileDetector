pipeline {
    agent any
    stages {
        stage('Set up virtualenv') {
            steps {
				withPythonEnv('/usr/bin/python3'){
				sh 'pip3 install -r requirements.txt'
				}
            }
            post {
                success {
                    echo "The virtual environment is set up successfully."
                }
            }
        }

        stage('Run unit tests'){
            steps{
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {    
                    sh 'python3 -m pytest tests'
                }
            }
        }

        
        stage('Run pylint'){
            steps{
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    sh 'python3 -m pylint efd'
                }
            }
        }
		stage('Run mypy'){
            steps{
                sh '/var/lib/jenkins/.local/bin/mypy efd'
            }
        }
    }
}