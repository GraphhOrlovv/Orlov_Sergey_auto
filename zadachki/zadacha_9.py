# Вернуть только совершеннолетних

users = [
{"name": "Daniil", "age": 30},
{"name": "Ivan", "age": 17},
{"name": "Anna", "age": 25}
]

users_dict_1 = list()

for user in users:
    if user["age"] >= 18:
        users_dict_1.append(user)

print(users_dict_1)

users_dict = list(filter(lambda x: x["age"] > 18, users))

print(users_dict)
