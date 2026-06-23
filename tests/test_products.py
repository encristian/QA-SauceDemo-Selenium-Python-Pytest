from pages.login_page import LoginPage
from pages.products_page import ProductsPage


VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


def login_as_standard_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    return ProductsPage(driver)


def test_products_page_is_displayed_after_login(driver):
    products_page = login_as_standard_user(driver)

    assert "inventory.html" in driver.current_url
    assert products_page.is_products_page_displayed()


def test_product_list_is_displayed(driver):
    products_page = login_as_standard_user(driver)

    assert products_page.get_products_count() > 0


def test_first_product_details_are_displayed(driver):
    products_page = login_as_standard_user(driver)

    product_name = products_page.get_first_product_name()
    product_price = products_page.get_first_product_price()

    assert product_name != ""
    assert product_price != ""
    assert "$" in product_price


def test_add_product_to_cart_updates_cart_badge(driver):
    products_page = login_as_standard_user(driver)

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_badge_text() == "1"
    assert products_page.is_remove_button_displayed()