pipeline{
    agent any
    stages{
        stage('test'){
            agent{
                docker{
                    image 'python:3'
                }
            }
            steps{
                echo 'Check if SCM is polled every minute'
                echo 'Peforming the unit tests'
                sh 'python3 -m unittest testsum_unittest.py'
                emailext body: 'Test Message',subject: 'Test Subject', to: 'pai.anusha23@gmail.com'
            }
        }
        stage('build'){
            steps{
                sh 'docker build -t python-app .'
            }

        }
        stage('deploy'){
            steps{
                echo 'Deploying the app'
                sh 'docker run python-app < inputfile.txt'
            }
        }
    }
}