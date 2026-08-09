data = {"name": "Ivan", "email": "", "age": 30}
# Нужно найти пустые значения.

a = []
for key, value in data.items():
    if isinstance(value, str):
        if not value.strip():
            a.append(key)
    elif not value:
        a.append(key)

print(a)
