# def printing_text(text: str, length: int, high: int):
#     if length - len(text) < 4:
#         raise TypeError("Длина текста должна быть меньше длины поля на 2 как минимум")
#     pustota = " "
#     left = right = pustota * ((length - len(text)) // 2 - 1)
#     sym = "#"
#     print(sym * length)
#     i = 0
#     while i != high // 2 - 1:
#         print(sym + " " * (length - 2) + sym)
#         i += 1
#     print(sym + left + text + right + pustota * (length % 2) + sym)
#     for _ in range(high // 2 - 1):
#         print(sym + " " * (length - 2) + sym)
#     print(sym * length)
#
#
# any_text = "Hello, World!"
# printing_text(any_text, 17, 5)
