from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 15", "+79991111111"),
    Smartphone("Samsung", "Galaxy S24", "+79992222222"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79993333333"),
    Smartphone("Huawei", "P60", "+79994444444"),
    Smartphone("Google", "Pixel 8", "+79995555555")
]

for smartphone in catalog:
    print(
        f"{smartphone.brand} - "
        f"{smartphone.model}. "
        f"{smartphone.phone_number}"
    )
