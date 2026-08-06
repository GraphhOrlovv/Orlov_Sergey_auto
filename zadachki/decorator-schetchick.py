import datetime
import time
def decor_schetchick(func):
    i = 0
    def wrapper(*args, **kwargs):
        nonlocal i
        i += 1
        start  = time.time()
        print(f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}: "
              f"Начало выполнения функции {func.__name__}")
        result = func(*args, **kwargs)
        end = time.time()
        time_func = end - start
        print(f"{datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}: "
              f"Конец выполнения функции {func.__name__}")
        print(f"Функция {func.__name__} выполнилась за: {time_func:.10f} сек")
        print(f"Функция {func.__name__} выполнилась {i} раз")
        return result
    return wrapper

@decor_schetchick
def multiply(nums):
    a = []
    for num in nums:
        a.append(num * 2)
    return a

multiply([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
multiply([1, 2, 3, 4, 5, 6, 7, 8, 9, 11])


# print(datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S'))