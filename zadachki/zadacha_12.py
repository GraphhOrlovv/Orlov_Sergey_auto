# Вернуть количество уникальный элементов

data = [1,2,2,3,4,4,4]

new_numbers = dict()
for number in data:
    new_numbers[number] = new_numbers.get(number, 0) + 1
print(new_numbers)

count = 0

for key, value in new_numbers.items():
    if new_numbers[key] == 1:
        count += 1
print(count)

# Или так:
print(len(set(data)))
