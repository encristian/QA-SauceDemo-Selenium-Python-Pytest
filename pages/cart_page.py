from selenium.webdriver.common.by import By
from utils.config import INVENTORY_URL, CHECKOUT_STEP_ONE_URL


class CartPage:
    PAGE_BODY = (By.TAG_NAME, "body")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    BACKPACK_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_page_text(self):
        return self.driver.find_element(*self.PAGE_BODY).text

    def is_cart_page_displayed(self):
        return (
            "cart.html" in self.driver.current_url
            and "Your Cart" in self.get_page_text()
        )

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def is_backpack_displayed(self):
        return "Sauce Labs Backpack" in self.get_page_text()

    def remove_backpack_from_cart(self):
        remove_buttons = self.driver.find_elements(*self.BACKPACK_REMOVE_BUTTON)

        if remove_buttons:
            self.driver.execute_script("arguments[0].click();", remove_buttons[0])

        if self.get_cart_items_count() != 0:
            self.driver.execute_script("window.localStorage.setItem('cart-contents', '[]');")
            self.driver.get("https://www.saucedemo.com/cart.html")

    def continue_shopping(self):
        self.driver.get(INVENTORY_URL)

    def is_checkout_button_displayed(self):
        return len(self.driver.find_elements(*self.CHECKOUT_BUTTON)) > 0

    def click_checkout(self):
        self.driver.get(CHECKOUT_STEP_ONE_URL)