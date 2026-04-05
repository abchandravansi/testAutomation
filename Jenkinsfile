pipeline {
    agent any

    environment {
        ENV = "docker"
        PLATFORM = "web"
        BROWSER = "chrome"

        // Docker compose network hostname
        SELENIUM_URL = "http://selenium:4444/wd/hub"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/<your-username>/<repo>.git'
                    ]]
                ])
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt

                # install your src package
                pip install -e .
                '''
            }
        }

        stage('Run Web Tests') {
            steps {
                sh '''
                . venv/bin/activate

                mkdir -p reports

                pytest tests/web/ \
                    -v \
                    --html=reports/web_report.html \
                    --self-contained-html
                '''
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/**/*', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Web tests PASSED ✅"
        }
        failure {
            echo "Web tests FAILED ❌"
        }
    }
}