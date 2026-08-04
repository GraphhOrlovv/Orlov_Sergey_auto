# Нужно проверить — все ли SUCCESS.

statuses = ["SUCCESS", "SUCCESS", "FAILED"]

def check(list_statuses):
    for elem in list_statuses:
        if elem != "SUCCESS":
            return False
        else:
            continue
    return True

print(check(statuses))

# 2 способ
print(statuses.count("SUCCESS") == len(statuses))

# 3 способ
print(all(status == "SUCCESS" for status in statuses))
