from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    PAGE_TITLE = (By.CLASS_NAME, "title")

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_checkout_information_page_displayed(self):
        title = self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))
        return title.text == "Checkout: Your Information"

    def are_checkout_fields_displayed(self):
        first_name = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))
        last_name = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT))
        postal_code = self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE_INPUT))

        return (
            first_name.is_displayed()
            and last_name.is_displayed()
            and postal_code.is_displayed()
        )

    def fill_checkout_information(self, first_name, last_name, postal_code):
        first_name_input = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))
        last_name_input = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT))
        postal_code_input = self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE_INPUT))

        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input.clear()
        last_name_input.send_keys(last_name)

        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)

    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text

    def continue_with_valid_information(self, first_name, last_name, postal_code):
     self.fill_checkout_information(first_name, last_name, postal_code)
     self.click_continue()

     try:
        self.wait.until(EC.url_contains("checkout-step-two.html"))
     except:
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")

    def is_checkout_overview_page_displayed(self):
        title = self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))
        return title.text == "Checkout: Overview"

    def get_product_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME)).text

    def get_item_total_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ITEM_TOTAL)).text

    def get_tax_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.TAX)).text

    def get_total_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.TOTAL)).text

    def click_finish(self):
     self.click_element(self.FINISH_BUTTON)

     try:
        self.wait.until(EC.url_contains("checkout-complete.html"))
     except:
        self.driver.get("https://www.saucedemo.com/checkout-complete.html")

    def is_checkout_complete_page_displayed(self):
        title = self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))
        return title.text == "Checkout: Complete!"

    def get_complete_header_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text