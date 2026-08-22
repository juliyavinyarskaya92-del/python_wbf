import pytest

from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


@pytest.mark.parametrize(
    "string, expected",
    [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("", ""),
        ("skyPro", "Skypro"),
        ("123abc", "123abc"),
    ],
)
def test_capitalize(string_utils, string, expected):
    assert string_utils.capitalize(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
        ("  hello world", "hello world"),
        ("", ""),
        ("   ", ""),
        (" skypro ", "skypro "),
    ],
)
def test_trim(string_utils, string, expected):
    assert string_utils.trim(string) == expected


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "P", True),
        ("SkyPro", "U", False),
        ("", "S", False),
        ("hello", "ll", True),
        ("hello", "z", False),
    ],
)
def test_contains(string_utils, string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("hello", "l", "heo"),
        ("hello", "z", "hello"),
        ("", "a", ""),
        ("aaaa", "a", ""),
    ],
)
def test_delete_symbol(string_utils, string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

