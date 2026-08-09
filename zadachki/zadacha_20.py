orders = [{"status": "new"}, {"status": "done"}, {"status": "new"}]
# Сгруппировать по статусу.

new_dict = dict()
for order in orders:
    for key, value in order.items():
        if value not in new_dict.keys():
            new_dict[value] = [order]
        else:
            new_dict[value].append(order)

print(new_dict)
