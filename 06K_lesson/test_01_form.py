from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_filing_the_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 30)
    firstname_input = wait.until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )
    firstname_input.send_keys("Иван")

    lastname_input = wait.until(
        EC.presence_of_element_located((By.NAME, "last-name"))
    )
    lastname_input.send_keys("Петров")

    address_input = wait.until(
        EC.presence_of_element_located((By.NAME, "address"))
    )
    address_input.send_keys("Ленина, 55-3")

    email_input = wait.until(
        EC.presence_of_element_located((By.NAME, "e-mail"))
    )
    email_input.send_keys("test@skypro.com")

    city_input = wait.until(
        EC.presence_of_element_located((By.NAME, "city"))
    )
    city_input.send_keys("Москва")

    country_input = wait.until(
        EC.presence_of_element_located((By.NAME, "country"))
    )
    country_input.send_keys("Россия")

    phone_input = wait.until(
        EC.presence_of_element_located((By.NAME, "phone"))
    )
    phone_input.send_keys("+7985899998787")

    job_input = wait.until(
        EC.presence_of_element_located((By.NAME, "job-position"))
    )
    job_input.send_keys("QA")

    company_input = wait.until(
        EC.presence_of_element_located((By.NAME, "company"))
    )
    company_input.send_keys("SkyPro")

    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    submit_button.click()

    zip_code_input = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

    assert "danger" in zip_code_input.get_attribute("class")

    company_input = wait.until(
        EC.presence_of_element_located((By.ID, "company"))
    )

    assert "success" in company_input.get_attribute("class")

    job_input = wait.until(
        EC.presence_of_element_located((By.ID, "job-position"))
    )
    assert "success" in job_input.get_attribute("class")

    phone_input = wait.until(
        EC.presence_of_element_located((By.ID, "phone"))
    )
    assert "success" in phone_input.get_attribute("class")

    country_input = wait.until(
        EC.presence_of_element_located((By.ID, "country"))
    )
    assert "success" in country_input.get_attribute("class")
    email_input = wait.until(
        EC.presence_of_element_located((By.ID, "e-mail"))
    )
    assert "success" in email_input.get_attribute("class")

    city_input = wait.until(
        EC.presence_of_element_located((By.ID, "city"))
    )
    assert "success" in city_input.get_attribute("class")

    address_input = wait.until(
        EC.presence_of_element_located((By.ID, "address"))
    )
    assert "success" in address_input.get_attribute("class")
    firstname_input = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    assert "success" in firstname_input.get_attribute("class")

    lastname_input = wait.until(
        EC.presence_of_element_located((By.ID, "last-name"))
    )
    assert "success" in lastname_input.get_attribute("class")

    driver.quit()
