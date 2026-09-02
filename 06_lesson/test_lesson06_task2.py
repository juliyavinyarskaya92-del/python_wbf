from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Edge()
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZGI3YWFlOGUtZjlmMC00NmNlLWExN2MtYTUyNTE3NWNiOWNm",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/vinni4ka")
    user_1_url = driver.current_url
    print("Пользователь 1:", user_1_url)
    assert user_1_url == "https://gitflic.ru/user/vinni4ka"

    driver.delete_all_cookies()

    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "OWI4MDEwMWEtNzE1ZS00YzgyLTg1ZmYtMWU5YmFkMzc1ZWIx",
        "domain": "gitflic.ru"
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/yulvin")
    user_2_url = driver.current_url
    print("Пользователь 2:", user_2_url)
    assert user_2_url == "https://gitflic.ru/user/yulvin"
    assert user_1_url != user_2_url
    driver.refresh()

    driver.quit()
