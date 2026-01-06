import pytest
import os
from selenium import webdriver

# פונקציה לתפיסת הפרמטרים משורת הפקודה (מה שג'נקינס שולח)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome, firefox, edge"
    )


@pytest.fixture
def driver(request):
    # 1. איזה דפדפן המשתמש ביקש?
    browser_name = request.config.getoption("--browser")

    # 2. הגדרות הגריד
    hub_host = os.environ.get('HUB_HOST', 'localhost')
    hub_port = os.environ.get('SELENIUM_PORT', '4444')
    hub_url = f"http://{hub_host}:{hub_port}/wd/hub"

    print(f"\nConnecting to Grid: {hub_url} | Browser: {browser_name}")

    options = None

    # 3. יצירת האופציות המתאימות
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    # 4. התחברות לדרייבר
    driver = webdriver.Remote(
        command_executor=hub_url,
        options=options
    )

    driver.implicitly_wait(10)

    yield driver  # העברת הדרייבר לטסט

    print("\nClosing driver...")
    driver.quit()
