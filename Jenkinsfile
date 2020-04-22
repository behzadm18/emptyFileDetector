pipeline {
    agent any
    stages {
        stage('Set up virtualenv') {
            steps {
				withPythonEnv('/usr/bin/python3')
				sh 'pip install -r requirements.txt'
            }
            post {
                success {
                    echo "The virtual environment is set up successfully."
                }
            }
        }
        stage('Run unit tests'){
            steps{
                sh 'python -m pytest tests'
            }
            
        }
        stage('Run pylint'){
            steps{
                sh 'python -m pylint efd'
            }
        }
		stage('Run mypy'){
            steps{
                echo "NOT DONE YET"
            }
        }
    }
}