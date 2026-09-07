pipeline {
    agent any 
  
    stages {
        stage('clone') {
            steps {
                git "https://github.com/raghvamsk216/flask-devops-project"
            }
        }
        
        stage('build Docker image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        } 

        stage('push to ECR') {
            steps {
                // Note: Replace ACCOUNT_ID with your actual 12-digit AWS Account ID
                sh '''
                aws ecr get-login-password --region ap-south-1 \
                | docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.ap-south-1.amazonaws.com

                docker tag flask-app:latest ACCOUNT_ID.dkr.ecr.ap-south-1.amazonaws.com/flask-devops-app:latest
                docker push ACCOUNT_ID.dkr.ecr.ap-south-1.amazonaws.com/flask-devops-app:latest
                ''' 
            }
        }
    } 
} 
