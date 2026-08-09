import random

# def generate_users(n):
#     names = ['Alice', 'Mark', 'John', 'Ivan', 'Max', 'Liza', 'Peter']
#     users = []
#     for i in range(1, n+1):
#         user = random.choice(names)
#         users.append({'id': i, 'name': user})
#     return users
#
# a = generate_users(5)
#
# print(a)

"""
С yield
"""


def generate_users(n):
    names = ["Alice", "Mark", "John", "Ivan", "Max", "Liza", "Peter"]
    for i in range(1, n + 1):
        yield {"id": i, "name": random.choice(names)}


for user in generate_users(10):
    print(user)
