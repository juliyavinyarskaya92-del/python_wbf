from address import Address
from mailing import Mailing
to_address: Address = Address(
    "123456",
    "Москва",
    "Ленина",
    "10",
    "25"
)

from_address = Address(
    "654321",
    "Санкт-Петербург",
    "Невский проспект",
    "20",
    "15"
)

mailing = Mailing(
    to_address,
    from_address,
    500,
    "AB123456789RU"
)
print(
    f"Отправление {mailing.track} "
    f"из {mailing.to_address.index}, "
    f"{mailing.to_address.city}, "
    f"{mailing.to_address.street}, "
    f"{mailing.to_address.house} - "
    f"{mailing.to_address.flat}"
)
