import pytest
from selenium import webdriver

from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(driver):

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    page = CalculatorPage(driver)

    page.set_delay(45)

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    page.wait_for_result("15")

    assert page.get_result() == "15"
