words = []
while True:
    word = input("Введите слово: ")
    if word == 'stop':
        break
    words.append(word)

result = ' '.join(words)
print("Результат соединения слов:", result)