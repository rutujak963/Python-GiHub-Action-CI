pipeline {
   agent { docker { image 'python:3.5.1' } }

   stages {
      stage('Build') {
        steps {
          echo 'Building...'
          echo "Running ${env.BUILD_ID} ${env.BUILD_DISPLAY_NAME} on ${env.NODE_NAME} and JOB ${env.JOB_NAME}"
          sh 'python --version'//sh 'pip install -r requirements.txt'
        }
   }
   stage('Test') {
     steps {
        echo 'Testing...'
        //sh 'pytest'
     }
   }
   stage('Deploy') {
     steps {
       echo 'Deploying...'
     }
   }
  }
}
