users = [
{"id":1,"active":True},
{"id":2,"active":False}
]
# Получить только активных

# active_users = []
# for user in users:
#     if user["active"] == True:
#         active_users.append(user)

# active_users = [user for user in users if user["active"]]

active_users = list(filter(lambda user: user["active"],users))

print(active_users)