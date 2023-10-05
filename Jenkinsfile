pipeline{
    agent none
    stages{
        stage('Build'){
            steps{
                echo 'Building the app'
            }
        }
        stage('test'){
            steps{
                echo 'testing the app'
                sh "pytest testsum_unittest.py"
            }
        }
        stage('deploy'){
            steps{
                echo 'Deploying the app'
                sh "python3 testsum.py"
            }
        }
    }
}