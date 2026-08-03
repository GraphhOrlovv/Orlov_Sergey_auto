import time

# def even_numbers(n):
#     return (i for i in range(n+1) if i % 2 == 0)
#
# for num in even_numbers(10):
#     print(num)

class Timer:
    def __init__(self):
        self.elapsed = None

    def __enter__(self):
        self.t1 = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t2 = time.time()
        self.elapsed = self.t2 - self.t1
        return self.elapsed

with Timer() as timer:
    time.sleep(1)

print(timer.elapsed)
