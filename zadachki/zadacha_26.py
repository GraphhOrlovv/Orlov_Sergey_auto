from typing import Any

data = {"user": {"profile": {"email": "test@test.com"}}}
# Получить email.


def find_value_by_key(any_dict: dict) -> Any:
    for key, value in any_dict.items():
        if key == "email":
            return value
        elif isinstance(value, dict):
            result = find_value_by_key(value)
            if result is not None:
                return result
    return "Ключа email в словаре data нет"


print(find_value_by_key(data))
