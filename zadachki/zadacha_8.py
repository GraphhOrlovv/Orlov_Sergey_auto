scores = {"Alice": 80, "Bob": 95, "Charlie": 70}

# b = dict()
# for i in sorted(scores.values()):
#     for key, value in scores.items():
#         if i == value:
#             b[key] = i
#
# print(b)

sorted_dict = dict(sorted(scores.items(), key=lambda x: x[1]))

print(sorted_dict)
