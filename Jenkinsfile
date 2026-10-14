pipeline {
    agent any
    triggers { githubPush() }
    stages {
        stage('Build') {
            steps {
                sh 'docker rm -f lr_api || true'
                sh 'docker compose down || true'
                sh 'docker compose pull'
                sh 'docker compose up -d'
            }
        }
    }
}
