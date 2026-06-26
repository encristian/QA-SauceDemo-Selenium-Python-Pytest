from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")

    BACKPACK_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BACKPACK_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

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
        self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ADD_TO_CART_BUTTON)).click()

    def is_remove_button_displayed(self):
        return self.driver.find_element(*self.BACKPACK_REMOVE_BUTTON).is_displayed()

    def get_cart_badge_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_BADGE)).text

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        self.wait.until(EC.url_contains("cart.html"))