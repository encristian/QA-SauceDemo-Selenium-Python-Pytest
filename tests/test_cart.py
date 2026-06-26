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

    driver.get("https://www.saucedemo.com/cart.html")

    return CartPage(driver)


def test_cart_page_is_displayed_after_clicking_cart_icon(driver):
    login_as_standard_user(driver)

    driver.get("https://www.saucedemo.com/cart.html")

    cart_page = CartPage(driver)

    assert cart_page.is_cart_page_displayed()


def test_product_is_displayed_in_cart_after_adding_it(driver):
    cart_page = add_backpack_and_open_cart(driver)

    assert cart_page.is_backpack_displayed()


def test_product_details_are_displayed_in_cart(driver):
    cart_page = add_backpack_and_open_cart(driver)

    cart_text = cart_page.get_page_text()

    assert "Sauce Labs Backpack" in cart_text
    assert "$29.99" in cart_text
    assert "1" in cart_text


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