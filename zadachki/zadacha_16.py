# Есть функция:
# def send_request():
# ...
# Нужно реализовать повтор запроса до 3 раз.
import requests


def send_request(url, tryies=0):
    while tryies > 0:
        try:
            request = requests.get(url)
            print(f"Всё ок, ответ: {request}")
            break
        except Exception as e:
            tryies -= 1
            print(f"Запрос не отработал, ошибка: {e}\nОсталось попыток: {tryies}")
            continue
    else:
        print("Количество ретраев истекло")

send_request("https://ya.rup/", tryies=3)
