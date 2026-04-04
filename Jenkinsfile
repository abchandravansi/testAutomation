pipeline {
    agent any

    environment {
        // -------- Execution Control --------
        ENV = "docker"                  // local | docker | staging
        PLATFORM = "web"                // web | android | ios
        BROWSER = "chrome"
        DEVICE = "default"

        // -------- Selenium / Appium --------
        SELENIUM_URL = "http://172.17.0.1:4444/wd/hub"
        APPIUM_URL = "http://127.0.0.1:4723/wd/hub"

        // -------- Timeouts --------
        IMPLICIT_WAIT = "5"
        PAGE_LOAD_TIMEOUT = "30"

        // -------- Logging --------
        LOG_LEVEL = "INFO"
        LOG_DIR = "reports/logs"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out code..."
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "Installing dependencies..."

                sh '''
                python3 -m venv venv
                . venv/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Verify Selenium Grid') {
            when {
                expression { env.PLATFORM == 'web' }
            }
            steps {
                echo "Checking Selenium Grid availability..."

                sh '''
                curl --fail ${SELENIUM_URL}/status || (echo "Selenium Grid not reachable" && exit 1)
                '''
            }
        }

        stage('Verify Appium Server') {
            when {
                expression { env.PLATFORM == 'android' || env.PLATFORM == 'ios' }
            }
            steps {
                echo "Checking Appium Server..."

                sh '''
                curl --fail ${APPIUM_URL}/status || (echo "Appium not reachable" && exit 1)
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running tests..."

                sh '''
                . venv/bin/activate

                pytest tests/ \
                    --maxfail=1 \
                    --disable-warnings \
                    --html=reports/report.html \
                    --self-contained-html
                '''
            }
        }

        stage('Archive Reports') {
            steps {
                echo "Archiving reports..."

                archiveArtifacts artifacts: 'reports/**/*', fingerprint: true
            }
        }
    }

    post {

        always {
            echo "Cleaning up workspace..."
        }

        success {
            echo "Build SUCCESS"
        }

        failure {
            echo "Build FAILED"
        }
    }
}