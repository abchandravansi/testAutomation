pipeline {
    agent any

    environment {
        // -------------------------------
        // Execution Config
        // -------------------------------
        ENV = "docker"
        PLATFORM = "web"
        BROWSER = "chrome"

        // -------------------------------
        // Selenium Grid
        // -------------------------------
        SELENIUM_URL = "http://selenium:4444/wd/hub"

        // -------------------------------
        // Timeouts
        // -------------------------------
        IMPLICIT_WAIT = "5"
        PAGE_LOAD_TIMEOUT = "30"

        // -------------------------------
        // Logging
        // -------------------------------
        LOG_LEVEL = "INFO"
        LOG_DIR = "reports/logs"
    }

    stages {

        // --------------------------------
        // FIX: Explicit Git Checkout
        // --------------------------------
        stage('Checkout Code') {
            steps {
                echo "Cloning repository..."

                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/abchandravansi/testAutomation.git'
                    ]]
                ])
            }
        }

        // --------------------------------
        // Setup Python
        // --------------------------------
        stage('Setup Environment') {
            steps {
                echo "Setting up Python environment..."

                sh '''
                python3 -m venv venv
                . venv/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        // --------------------------------
        // Validate Selenium Grid
        // --------------------------------
        stage('Check Selenium Grid') {
            steps {
                echo "Checking Selenium availability..."

                sh '''
                curl --fail ${SELENIUM_URL}/status \
                || (echo "Selenium Grid NOT reachable" && exit 1)
                '''
            }
        }

        // --------------------------------
        // Run Tests
        // --------------------------------
        stage('Run Tests') {
            steps {
                echo "Executing tests..."

                sh '''
                . venv/bin/activate

                mkdir -p reports

                pytest tests/web/ \
                    --maxfail=1 \
                    --disable-warnings \
                    --html=reports/report.html \
                    --self-contained-html
                '''
            }
        }

        // --------------------------------
        // Archive Reports
        // --------------------------------
        stage('Archive Reports') {
            steps {
                echo "Archiving reports..."

                archiveArtifacts artifacts: 'reports/**/*', fingerprint: true
            }
        }
    }

    post {

        always {
            echo "Cleaning workspace..."
        }

        success {
            echo "Build SUCCESS ✅"
        }

        failure {
            echo "Build FAILED ❌"
        }
    }
}