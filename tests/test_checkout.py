from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE,
    BACKPACK_NAME,
    BACKPACK_PRICE,
    CHECKOUT_FIRST_NAME_ERROR,
    ORDER_COMPLETE_MESSAGE,
)


def login_as_standard_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    return ProductsPage(driver)


def start_checkout_with_backpack(driver):
    products_page = login_as_standard_user(driver)

    products_page.add_backpack_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    return CheckoutPage(driver)


def test_checkout_information_page_is_displayed(driver):
    checkout_page = start_checkout_with_backpack(driver)

    assert "checkout-step-one.html" in driver.current_url
    assert checkout_page.is_checkout_information_page_displayed()


def test_checkout_form_fields_are_displayed(driver):
    checkout_page = start_checkout_with_backpack(driver)

    assert checkout_page.are_checkout_fields_displayed()


def test_checkout_with_empty_form_shows_error_message(driver):
    checkout_page = start_checkout_with_backpack(driver)

    checkout_page.click_continue()

    error_message = checkout_page.get_error_message()

    assert CHECKOUT_FIRST_NAME_ERROR in error_message


def test_checkout_with_valid_information_opens_overview_page(driver):
    checkout_page = start_checkout_with_backpack(driver)

    checkout_page.continue_with_valid_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    assert "checkout-step-two.html" in driver.current_url
    assert checkout_page.is_checkout_overview_page_displayed()


def test_checkout_overview_displays_product_and_price_information(driver):
    checkout_page = start_checkout_with_backpack(driver)

    checkout_page.continue_with_valid_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    assert checkout_page.get_product_name() == BACKPACK_NAME
    assert BACKPACK_PRICE in checkout_page.get_item_total_text()
    assert "Tax:" in checkout_page.get_tax_text()
    assert "Total:" in checkout_page.get_total_text()


def test_complete_order_shows_confirmation_message(driver):
    checkout_page = start_checkout_with_backpack(driver)

    checkout_page.continue_with_valid_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    checkout_page.click_finish()

    assert "checkout-complete.html" in driver.current_url
    assert checkout_page.is_checkout_complete_page_displayed()
    assert checkout_page.get_complete_header_text() == ORDER_COMPLETE_MESSAGE