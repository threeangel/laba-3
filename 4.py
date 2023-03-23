import random

correct_answers = 0
wrong_answers = 0

while wrong_answers < 3:
    num1 = str(random.randint(1, 10))
    num2 = str(random.randint(1, 10))
    answer = str(input("Решите пример: " + num1 + " + " + num2 + " = "))

    if int(answer) == int(num1) + int(num2):
        print("Правильно!")
        correct_answers += 1
    else:
        print("Ответ неверный")
        wrong_answers += 1

print("Игра окончена. Правильных ответов: ", correct_answers)