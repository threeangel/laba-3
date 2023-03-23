result = ""
while True:
    word = input("Введите слово или 'stop' для окончания: ")
    result += word + " "
    if word == "stop":
        break
print("Результат:", result)