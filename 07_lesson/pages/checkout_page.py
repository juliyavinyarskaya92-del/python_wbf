from selenium.webdriver.common.by import By


class CheckoutPage:

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")

    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def fill_first_name(self, first_name):
        element = self.driver.find_element(*self.FIRST_NAME_INPUT)
        element.send_keys(first_name)

    def fill_last_name(self, last_name):
        element = self.driver.find_element(*self.LAST_NAME_INPUT)
        element.send_keys(last_name)

    def fill_postal_code(self, postal_code):
        element = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        element.send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self):
        total_text = self.driver.find_element(*self.TOTAL).text
        return total_text.replace("Total: ", "")
