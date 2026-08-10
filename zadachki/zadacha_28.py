numbers = [2, 4, 6, 8]

# Проверить — все ли чётные.

# print(all(num % 2 == 0 for num in numbers))

# flag = True
# while flag:
#     for num in numbers:
#         if not (num % 2 == 0):
#             print("Не все числа делятся на 2")
#             flag = False
#     else:
#         print("Да, все чётные")

for num in numbers:
    if num % 2 != 0:
        print("Не все числа чётные")
        break
else:
    print("Все числа чётные")
