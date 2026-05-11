pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
             git branch: 'main', url: 'https://github.com/Chris-coru/devops-158-JCR-tp.git'
            }
        }

        stage('Install') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install flask pytest
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                python3 -m pytest test_app.py
                '''
            }
        }


        stage('Run Flask') {
            steps {
                sh '''
                pkill -f "python3 app.py" || true
                . venv/bin/activate
                nohup python3 app.py > flask.log 2>&1 &
                sleep 2
                '''
            }
        }
    }
}
