pipeline{
    agent any
    stages{
        stage('build'){
            steps{
                sh 'docker build -t python-app .'
            }

        }
        stage('test'){
            steps{
                echo 'testing the app'
            }
        }
        stage('deploy'){
            steps{
                echo 'Deploying the app'
                sh 'docker run -i python-app'
            }
        }
    }
}