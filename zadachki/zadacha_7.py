data = [[1, 2], [3, 4], [5]]

result = []

for item in data:
    for num in item:
        if num not in result:
            result.append(num)

print(result)
