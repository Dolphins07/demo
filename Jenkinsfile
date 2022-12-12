
Jenkinsfile (Declarative Pipeline)

/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'sudo git pull
                sh 'sudo kill -9 `sudo lsof -t -i:6001`'
                sh 'sudo daphne -b 0.0.0.0 -p 6001 Speak2Learn.asgi:application  > log.txt & disown -h'
            }
        }
    }
}

