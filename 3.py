while True:
    word = input("Введите слово или 'stop' для выхода: ")
    if word == "stop":
        break
    if "ф" in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")