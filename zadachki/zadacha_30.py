user = {"id": 1, "password": "123", "token": "abc"}
# Удалить sensitive данные.

sensitive_data = {"password", "token", "ergergr"}

# for data in sensitive_data:
#     if data in user:
#         user.pop(data)
#
# print(user)

new_dict = {key: value for key, value in user.items() if key not in sensitive_data}

print(new_dict)
