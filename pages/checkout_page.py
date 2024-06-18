from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.continue_button = (By.ID, "continue")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        ).text
