pipeline {

    parameters {

        string(

            name: 'MI_PARAM',

            defaultValue: '',

            description: 'Parámetro opcional para el script'

        )

    }
 
    agent any
 
    stages {

        stage('Setup') {

            steps {

                sh '''

                    if [ ! -d "venv" ]; then

                        echo "Creando entorno virtual..."

                        python3 -m venv venv

                    else

                        echo "Entorno virtual ya existe, reutilizando..."

                    fi
 
                    . venv/bin/activate

                    pip install --upgrade pip

                '''

            }

        }
 
        
 
        stage('Ejecutar script') {
  steps {
    sh '''#!/bin/bash
      set -e

      # (si no existe el venv, créalo)
      [ -d venv ] || python3 -m venv venv

      . venv/bin/activate

      # si tienes dependencias:
      # pip install -r requirements.txt

      if [ -n "${MI_PARAM:-}" ]; then
        python Python.py "$MI_PARAM"
      else
        python Python.py
      fi
    '''
  }
}


    }

}
 

