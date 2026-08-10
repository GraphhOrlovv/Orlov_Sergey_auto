names = ["Ivan", "Anna"]
# Сделать:
# {"Ivan":0,"Anna":1}

dict_names = dict()

for i in range(len(names)):
    dict_names[names[i]] = i

print(dict_names)
