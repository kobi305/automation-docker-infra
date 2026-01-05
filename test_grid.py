import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# הגדרות כלליות
hub_url = os.environ.get("SELENIUM_HUB_URL", "http://localhost:4444")

# --- Fixture: הפונקציה הזו רצה אוטומטית לפני ואחרי כל טסט ---


@pytest.fixture
def driver():
    print(f"\nConnecting to Selenium Grid at: {hub_url}")
    options = webdriver.ChromeOptions()

    # חיבור ל-Grid
    driver = webdriver.Remote(command_executor=hub_url, options=options)
    driver.implicitly_wait(10)

    yield driver  # כאן הטסט עצמו רץ

    # החלק הזה קורה אחרי שהטסט נגמר (Teardown)
    print("\nClosing driver...")
    driver.quit()

# --- הטסט עצמו ---


def test_google_search(driver):
    print("1. Navigating to Google...")
    driver.get("https://www.google.com")

    print(f"2. Page Title is: {driver.title}")
    assert "Google" in driver.title, "Title does not contain 'Google'"

    # צילום מסך במקרה של הצלחה (אפשר גם להגדיר רק בכישלון)
    # אנחנו שומרים אותו בתיקייה שמופת החוצה
    reports_dir = "allure-results"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    print("Test Finished Successfully!")
    print("Auto Trigger Works Now!")
