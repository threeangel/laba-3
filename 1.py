n = int(input("Введите кол-во слов: "))
result = ""

for i in range(n):
    word = input("Напиши слово: ")
    result += word + " "

print("Результат:", result)