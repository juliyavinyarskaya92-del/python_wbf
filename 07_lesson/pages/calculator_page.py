from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, delay):
        element = self.driver.find_element(*self.DELAY_INPUT)
        element.clear()
        element.send_keys(delay)

    def click_button(self, value):
        button = self.driver.find_element(
            By.XPATH,
            f"//button[text()='{value}']"
        )
        button.click()

    def wait_for_result(self, result, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.RESULT,
                result
            )
        )

    def get_result(self):
        return self.driver.find_element(*self.RESULT).text
