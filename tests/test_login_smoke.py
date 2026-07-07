from pages.login_page import LoginPage
from utils.test_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    LOGIN_ERROR_MESSAGE,
)


def test_login_page_is_displayed(driver):
    login_page = LoginPage(driver)

    login_page.open()

    assert "Swag Labs" in driver.title
    assert login_page.is_login_page_displayed()


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    assert "inventory.html" in driver.current_url


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    error_message = login_page.get_error_message()

    assert LOGIN_ERROR_MESSAGE in error_message