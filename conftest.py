import os
from datetime import datetime

import pytest
from pytest_html import extras
from selenium import webdriver


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()

    if os.getenv("CI") == "true":
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    browser.implicitly_wait(5)

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is not None:
            screenshots_folder = os.path.join("reports", "screenshots")
            os.makedirs(screenshots_folder, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_folder, screenshot_name)

            driver.save_screenshot(screenshot_path)

            report.extras = getattr(report, "extras", [])
            report.extras.append(extras.image(screenshot_path))