class Math_Operations:

    def divide(self, a, b):
        if not isinstance(a, int | float) or not isinstance(b, int | float):
            raise TypeError("Здесь должны быть только числа")
        elif b == 0:
            raise ZeroDivisionError("Делить на ноль нельзя!")
        return a / b


# res = Math_Operations()
#
# print(res.divide(5, 4))
