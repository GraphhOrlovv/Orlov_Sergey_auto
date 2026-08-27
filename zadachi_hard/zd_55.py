def decor_func(func):
    def wrapper(*args, **kwargs):
        print("Something first")
        func(*args, **kwargs)
        print("Something second")
    return wrapper

@decor_func
def say_hello():
    print("hello")

say_hello()