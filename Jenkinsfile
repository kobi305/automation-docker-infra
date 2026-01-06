pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    // יצירת קובץ הסביבה
                    sh 'echo "SELENIUM_PORT=4445" > .env'
                    sh 'echo "HUB_HOST=selenium-hub" >> .env'
                    
                    // ניקוי ריצות קודמות
                    sh 'rm -rf allure-results'
                    sh 'mkdir -p allure-results'
                }
            }
        }

        stage('Build Image') {
            steps {
                // בניית האימג' מחדש כדי לקלוט שינויי קוד
                sh 'docker-compose -p dockers build test-runner'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // ניקוי קונטיינר ישן אם נתקע
                    sh 'docker rm -f temp-runner || true'
                    
                    // הרצת הטסטים
                    // הוספנו "|| true" כדי שגם אם יש באג בטסט, הג'נקינס ימשיך לשלב הדוח ולא יעצור מיד
                    sh 'docker-compose -p dockers run --name temp-runner test-runner pytest --alluredir=/app/allure-results || true'
                }
            }
        }
        
        stage('Extract Results') {
            steps {
                // העתקת הדוחות מהקונטיינר החוצה
                sh 'docker cp temp-runner:/app/allure-results/. ./allure-results/'
                
                // ניקוי הקונטיינר
                sh 'docker rm -f temp-runner'
            }
        }
    }

    post {
        always {
            // יצירת דוח Allure - גם אם הטסטים נכשלו
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}