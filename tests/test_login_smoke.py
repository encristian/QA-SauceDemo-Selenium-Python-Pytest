from pages.login_page import LoginPage


def test_login_page_is_displayed(driver):
    login_page = LoginPage(driver)

    login_page.open()

    assert "Swag Labs" in driver.title
    assert login_page.is_login_page_displayed()


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("invalid_user", "wrong_password")

    error_message = login_page.get_error_message()

    assert "Username and password do not match" in error_message