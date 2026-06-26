from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


def login_as_standard_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    return ProductsPage(driver)


def add_backpack_and_open_cart(driver):
    products_page = login_as_standard_user(driver)

    products_page.add_backpack_to_cart()
    products_page.open_cart()

    return CartPage(driver)


def test_cart_page_is_displayed_after_clicking_cart_icon(driver):
    products_page = login_as_standard_user(driver)

    products_page.open_cart()

    cart_page = CartPage(driver)

    assert "cart.html" in driver.current_url
    assert cart_page.is_cart_page_displayed()


def test_product_is_displayed_in_cart_after_adding_it(driver):
    cart_page = add_backpack_and_open_cart(driver)

    assert cart_page.is_backpack_displayed()


def test_product_details_are_displayed_in_cart(driver):
    cart_page = add_backpack_and_open_cart(driver)

    assert cart_page.get_backpack_name() == "Sauce Labs Backpack"
    assert cart_page.get_backpack_price() == "$29.99"
    assert cart_page.get_backpack_quantity() == "1"


def test_remove_product_from_cart(driver):
    cart_page = add_backpack_and_open_cart(driver)

    cart_page.remove_backpack_from_cart()

    assert cart_page.get_cart_items_count() == 0


def test_continue_shopping_redirects_to_products_page(driver):
    cart_page = add_backpack_and_open_cart(driver)

    cart_page.continue_shopping()

    products_page = ProductsPage(driver)

    assert "inventory.html" in driver.current_url
    assert products_page.is_products_page_displayed()