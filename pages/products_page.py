from selenium.webdriver.common.by import By


class ProductsPage:
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")

    BACKPACK_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BACKPACK_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def is_products_page_displayed(self):
        title = self.driver.find_element(*self.PRODUCTS_TITLE)
        return title.is_displayed() and title.text == "Products"

    def get_products_count(self):
        products = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(products)

    def get_first_product_name(self):
        return self.driver.find_element(*self.FIRST_PRODUCT_NAME).text

    def get_first_product_price(self):
        return self.driver.find_element(*self.FIRST_PRODUCT_PRICE).text

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.BACKPACK_ADD_TO_CART_BUTTON).click()

    def is_remove_button_displayed(self):
        return self.driver.find_element(*self.BACKPACK_REMOVE_BUTTON).is_displayed()

    def get_cart_badge_text(self):
        return self.driver.find_element(*self.CART_BADGE).text