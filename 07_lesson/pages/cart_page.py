from selenium.webdriver.common.by import By


class CartPage:
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def get_items(self):
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [element.text for element in elements]

    def item_is_in_cart(self, product_name):
        items = self.get_items()
        return product_name in items

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
