words = ["api", "automation", "test", "qa"]
# Оставить только слова длиннее 3 символов.

# for word in words:
#     if not len(word) > 3:
#         words.remove(word)

filtered_words = [word for word in words if len(word) > 3]

print(filtered_words)
