pipeline{
    agent{
        docker{
            image 'python:3'
        }
    }
    stages{
        stage('Checkout'){
            steps{
                checkout scmGit(
                    branches: [[name: 'main']],
                    userRemoteConfigs: [[url: 'https://github.com/anushapai23/demo-cicd']])
            }
        }
        stage('Build'){
            steps{
                echo 'Building the app'
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
                sh 'python3 testsum.py< inputfile.txt'
            }
        }
    }
}