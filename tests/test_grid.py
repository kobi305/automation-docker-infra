import os

# שים לב: הטסט מקבל את ה-driver אוטומטית מ-conftest.py
# אין צורך לייבא לכאן את webdriver או pytest


def test_google_search(driver):
    print("1. Navigating to Google...")
    driver.get("https://www.google.com")

    print(f"2. Page Title is: {driver.title}")
    assert "Google" in driver.title, "Title does not contain 'Google'"

    # יצירת תיקיית דוחות
    # שינינו מעט את הנתיב כדי שיתאים למבנה החדש
    reports_dir = "/app/allure-results"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    print("Test Finished Successfully!")
