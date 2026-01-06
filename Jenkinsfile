pipeline {
    agent any

    // כאן אנחנו מגדירים את התפריט שיופיע למשתמש
    parameters {
        choice(name: 'BROWSER', choices: ['chrome', 'firefox', 'edge'], description: 'Select Browser')
        // הוספנו גם אופציה לבחור תגיות (למשל סאניטי) - כרגע נשאיר ריק כדי להריץ הכל
        string(name: 'MARKER', defaultValue: '', description: 'Pytest Marker (e.g., sanity, regression). Leave empty for all.')
    }

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // שימוש בפרמטר שבחר המשתמש
                    // params.BROWSER - יכיל את מה שבחרת בתפריט
                    sh "echo 'SELENIUM_PORT=4445' > .env"
                    sh "echo 'HUB_HOST=selenium-hub' >> .env"
                    
                    // כאן אנחנו מזריקים את הבחירה שלך למשתני הסביבה
                    sh "echo 'BROWSER=${params.BROWSER}' >> .env"
                    
                    sh 'rm -rf allure-results'
                    sh 'mkdir -p allure-results'
                }
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker-compose -p dockers build test-runner'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker rm -f temp-runner || true'
                    
                    // בניית הפקודה הדינמית
                    def pytestCommand = "pytest --alluredir=/app/allure-results --browser=${params.BROWSER}"
                    
                    // אם המשתמש כתב משהו ב-MARKER, נוסיף אותו לפקודה
                    if (params.MARKER != '') {
                        pytestCommand += " -m ${params.MARKER}"
                    }

                    // הרצת הפקודה שהרכבנו
                    sh "docker-compose -p dockers run --name temp-runner test-runner ${pytestCommand} || true"
                }
            }
        }
        
        stage('Extract Results') {
            steps {
                sh 'docker cp temp-runner:/app/allure-results/. ./allure-results/'
                sh 'docker rm -f temp-runner'
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}