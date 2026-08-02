# 1 способ:
# def search_num(numbers: list):
#     new_num = set()
#     for num in numbers:
#         try:
#             new_num.add(num)
#         except ValueError("Ошибка") as e:
#             return e
#         continue


def search_num(numbers: list):
    if len(numbers) == len(set(numbers)):
        return False
    return True


list_numbers = [1, 2, 3, 4]
print(search_num(list_numbers))
