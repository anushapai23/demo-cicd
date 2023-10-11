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
                sh 'sudo python3 -m pip install flake8'
                echo 'Peforming the unit tests'
                sh 'python3 -m unittest testsum_unittest.py'
                echo 'Performing the lint tests'
                sh 'flake8 .'
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