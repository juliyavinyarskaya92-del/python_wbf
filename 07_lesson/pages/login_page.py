from selenium.webdriver.common.by import By


class LoginPage:

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        element = self.driver.find_element(*self.USERNAME_INPUT)
        element.send_keys(username)

    def enter_password(self, password):
        element = self.driver.find_element(*self.PASSWORD_INPUT)
        element.send_keys(password)

    def click_login(self):
        button = self.driver.find_element(*self.LOGIN_BUTTON)
        button.click()
