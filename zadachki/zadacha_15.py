response = {
"status_code": 200,
"body": {"message": "ok"}
}
# Нужно написать функцию валидации.

def is_valid(any_response):
    if any_response["status_code"] != 200:
        return (f"Ошибка! Статус код не равен 200, "
                f"его текущее значение = {any_response['status_code']}")
    if any_response["body"]["message"] != "ok":
        return (f"Ошибка! сообщение не ок")
    return True

print(is_valid(response))
