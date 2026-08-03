numbers = [1, 2, 2, 3, 4, 4, 5]

# new_list = set(numbers)
#
# our_list = list(new_list)
#
# print(our_list)

new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)

print(new_list)
