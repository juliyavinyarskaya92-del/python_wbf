import pytest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page = InventoryPage(driver)

    inventory_page.add_product("Sauce Labs Backpack")
    inventory_page.add_product("Sauce Labs Bolt T-Shirt")
    inventory_page.add_product("Sauce Labs Onesie")

    inventory_page.go_to_cart()

    cart_page = CartPage(driver)

    assert cart_page.item_is_in_cart("Sauce Labs Backpack")
    assert cart_page.item_is_in_cart("Sauce Labs Bolt T-Shirt")
    assert cart_page.item_is_in_cart("Sauce Labs Onesie")

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    checkout_page.fill_first_name("Ivan")
    checkout_page.fill_last_name("Ivanov")
    checkout_page.fill_postal_code("123456")

    checkout_page.click_continue()

    total = checkout_page.get_total()

    assert total == "$58.29"
