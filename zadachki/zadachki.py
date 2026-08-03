# Есть список ID пользователей.

# ```python
ids = [101, 203, 101, 405, 203, 999, 101]
# ```

# Нужно написать функцию, которая возвращает **все дубликаты**.

# def return_duplicate(our_list: list):
#     list_with_no_duplicate = []
# #     for num in our_list:
# #         if num not in list_with_no_duplicate:
# #             list_with_no_duplicate.append(num)
# #     return list_with_no_duplicate
#     for i in range(len(our_list)):
#         if (our_list[i] in our_list[i+1:]
#         and our_list[i]
#                 not in list_with_no_duplicate):
#             list_with_no_duplicate.append(our_list[i])
#     return list_with_no_duplicate
#
# print(return_duplicate(ids))

# Дана строка:

# ```python
# text = "pytest is awesome"
# ```

# Нужно вернуть:

# ```
# awesome is pytest
# ```

# new_text = text.split()
# print(' '.join(new_text[::-1]))

# 2. Подсчёт количества слов

# Есть строка:

# ```python
text = "python pytest automation python api test"
# ```

# Нужно вернуть словарь:

# ```
{"python": 2, "pytest": 1, "automation": 1, "api": 1, "test": 1}
# ```

text_dict = dict()
for word in text.split():
    text_dict[word] = text_dict.get(word, 0) + 1


print(text_dict)
