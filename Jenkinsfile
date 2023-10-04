pipeline{
    agent none
    stages{
        stage('Build'){
            steps{
                echo 'Building the app'
                sh 'docker build -t python-app .'
                sh 'docker run -ti python-app'
                echo '1,2'
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
            }
        }
    }
}