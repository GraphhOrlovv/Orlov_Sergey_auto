user = {"id": 1, "name": "Ivan"}
# Проверить обязательные поля:
required_fields = ["id", "name", "email"]

if all(field in user.keys() for field in required_fields):
    print("Всё ок")
else:
    print("Не все поля есть")
