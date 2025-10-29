pipeline{
    agent any
    stages{
        stage ("Build Image"){
            steps{
                echo "Build Docker Image"
                bat "docker build -t kubeapp:latest ."
            }
        }
  
        stage("push Image to Docker"){
            steps {
                echo "login to docker"
                bat "docker login -u vaishnavikarra -p Harekrishna8*"
                echo "push image to docker "
                bat "docker tag  vaishnavikarra/kubeapp:latest"
                bat "docker push vaishnavikarra/kubeapp"


            }
        }
        stage("Deploy"){
            steps{
                bat "kubectl  deployment.yaml --validate=false"
                bat "kubectl  service.yaml"
            }
        }
    }
    post{
        success{
            echo 'Pipeline completed scucessfully'

        }
        failure{
            echo "Pipeline failed"
        }
    }
}