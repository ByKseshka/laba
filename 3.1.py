N = int(input("Введите количество слов: "))
words = []
for i in range(N):
    word = input(f"Введите слово {i + 1}: ")
    words.append(word)
result = ' '.join(words)
print("Результат соединения слов:", result)