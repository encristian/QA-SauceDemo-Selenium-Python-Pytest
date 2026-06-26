from selenium.webdriver.common.by import By


class CartPage:
    CART_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    BACKPACK_NAME = (
        By.XPATH,
        "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']"
    )

    BACKPACK_PRICE = (
        By.XPATH,
        "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']"
        "/ancestor::div[@class='cart_item']//div[@class='inventory_item_price']"
    )

    BACKPACK_QUANTITY = (
        By.XPATH,
        "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']"
        "/ancestor::div[@class='cart_item']//div[@class='cart_quantity']"
    )

    BACKPACK_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def is_cart_page_displayed(self):
        title = self.driver.find_element(*self.CART_TITLE)
        return title.is_displayed() and title.text == "Your Cart"

    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def is_backpack_displayed(self):
        backpack_items = self.driver.find_elements(*self.BACKPACK_NAME)
        return len(backpack_items) > 0

    def get_backpack_name(self):
        return self.driver.find_element(*self.BACKPACK_NAME).text

    def get_backpack_price(self):
        return self.driver.find_element(*self.BACKPACK_PRICE).text

    def get_backpack_quantity(self):
        return self.driver.find_element(*self.BACKPACK_QUANTITY).text

    def remove_backpack_from_cart(self):
        self.driver.find_element(*self.BACKPACK_REMOVE_BUTTON).click()

    def continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()

    def is_checkout_button_displayed(self):
        return self.driver.find_element(*self.CHECKOUT_BUTTON).is_displayed()