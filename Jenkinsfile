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
 
        stage('Instalar requirements') {

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
 
                    if [ -n "$MI_PARAM" ]; then

                        python3 main.py "$MI_PARAM"

                    else

                        python3 main.py

                    fi

                '''

            }

        }

    }

}
 
