from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_sort_dropdown = (By.CSS_SELECTOR, ".product_sort_container")
        self.product_prices = (By.CSS_SELECTOR, ".inventory_item_price")
        self.add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
        self.remove_button = (By.XPATH, "//button[text()='Remove']")
        self.cart_button = (By.ID, "shopping_cart_container")

    def sort_products_low_to_high(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.product_sort_dropdown)
        )
        dropdown.click()
        self.driver.find_element(By.XPATH, "//option[text()='Price (low to high)']").click()

    def get_first_product_price(self):
        prices = self.driver.find_elements(*self.product_prices)
        return prices[0].text

    def add_first_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def is_remove_button_displayed(self):
        return self.driver.find_element(*self.remove_button).is_displayed()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
