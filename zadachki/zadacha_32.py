import pytest

email = "user@test.com"
# Написать функцию проверки.


@pytest.fixture
def any_email():
    return email


def test_email(any_email):
    symbols = [".com", ".ru"]
    assert "@" in any_email, "Нету @"
    assert any(sym in any_email for sym in symbols)
    assert any_email[len(any_email) - 4] == "." or any_email[len(any_email) - 5] == "."


# print(email[12])
