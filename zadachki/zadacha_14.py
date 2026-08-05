# Есть ответ API:
response = {
"status": "success",
"data": {
"user_id": 10,
"email": "test@test.com"
}
}
# Нужно проверить наличие обязательных полей.

required_fields = ["status","data","user_id", "email"]

def all_fields(any_response):
    fields = []
    for obj in any_response.items():
        fields.append(obj[0])
        if isinstance(obj[1], dict):
            fields.extend(all_fields(obj[1]))
    return fields

def check_all_fields(any_required_fields, our_response):
    fields = all_fields(our_response)
    missing_fields = [field for field in any_required_fields if field not in fields]
    if missing_fields:
        return f"Потерянные ключи: {missing_fields}"
    return "Всё чётко!"

print(check_all_fields(required_fields, response))


