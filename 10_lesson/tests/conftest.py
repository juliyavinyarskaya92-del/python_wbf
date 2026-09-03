import allure
import pytest
import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture(scope="function")
def chrome_driver():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    geckodriver_path = r"C:\Users\Honor\Desktop\Puton\domaska\geckodriver.exe"
    service = Service(geckodriver_path)
    with allure.step("Запуск Firefox браузера"):
        driver = webdriver.Firefox(service=service, options=options)
        driver.implicitly_wait(10)
    yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()
