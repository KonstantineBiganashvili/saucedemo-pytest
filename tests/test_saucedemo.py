import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import random
import string

@allure.feature("SauceDemo Tests")
class TestSauceDemo:
    @allure.story("Login with valid credentials")
    def test_login_valid(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url

    @allure.story("Login with invalid credentials")
    def test_login_invalid(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        invalid_username = ''.join(random.choices(string.ascii_lowercase, k=10))
        invalid_password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        login_page.login(invalid_username, invalid_password)
        error_message = login_page.get_error_message()
        assert "Username and password do not match" in error_message

    @allure.story("Sort products and validate")
    def test_sort_products_low_to_high(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.sort_products_low_to_high()
        first_product_price = inventory_page.get_first_product_price()
        inventory_page.add_first_product_to_cart()
        assert inventory_page.is_remove_button_displayed()

        inventory_page.go_to_cart()
        cart_price = cart_page.get_cart_item_price()
        cart_name = cart_page.get_cart_item_name()
        assert first_product_price == cart_price
        assert "Sauce Labs" in cart_name

        cart_page.go_to_checkout()
        checkout_page.click_continue()
        error_message = checkout_page.get_error_message()
        assert "Error: First Name is required" in error_message
