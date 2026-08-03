import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        func_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {func_time}")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Готово!"

print(slow_function())