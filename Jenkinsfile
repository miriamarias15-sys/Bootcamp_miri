pipeline {
  agent any

  parameters {
    string(name: 'NOMBRE', defaultValue: 'Miriam Arias', description: 'Variable definida por el usuario')
  }

  stages {

    stage('Info') {
      steps {
        echo "Hola, ${params.NOMBRE}"
        echo "JOB_NAME=${env.JOB_NAME}"
        echo "BUILD_NUMBER=${env.BUILD_NUMBER}"
        echo "NODE_NAME=${env.NODE_NAME}"
        echo "WORKSPACE=${env.WORKSPACE}"
      }
    }

    stage('Crear entorno virtual') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          python -m pip install --upgrade pip
        '''
      }
    }

    stage('Instalar requirements.txt') {
      steps {
        sh '''
          . venv/bin/activate
          pip install -r requirements.txt
        '''
      }
    }

    stage('Ejecutar script') {
      steps {
        sh '''
          . venv/bin/activate
          python Python.py "$NOMBRE"
        '''
  }
}

  }
}



