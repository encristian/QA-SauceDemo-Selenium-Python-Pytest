from selenium.webdriver.common.by import By


def test_login_page_is_displayed(driver):
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    assert "Swag Labs" in driver.title
    assert username_input.is_displayed()
    assert password_input.is_displayed()
    assert login_button.is_displayed()