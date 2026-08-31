from selenium.webdriver.common.by import By


class InventoryPage:

    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self, product_name):
        button = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='inventory_item']//button"
        )
        button.click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
