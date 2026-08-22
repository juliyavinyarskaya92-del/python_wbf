from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Edge()
    driver.get("https://httpbin.qa-territory.online/")
    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()
    url = "https://httpbin.qa-territory.online/forms/post"
    assert driver.current_url == url
    driver.back()
    assert driver.current_url == "https://httpbin.qa-territory.online/"
    driver.quit()
