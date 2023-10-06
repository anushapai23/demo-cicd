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
                sh "python3 -m unittest testsum_unittest.py"
            }
        }
        stage('deploy'){
            steps{
                echo 'Deploying the app'
                sh 'docker run -ti python-app'
            }
        }
    }
}