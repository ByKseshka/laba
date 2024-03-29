import random
def math_game():
    correct_answers = 0
    wrong_answers = 0

    while wrong_answers < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        else:
            result = num1 * num2

        user_answer = input(f"{num1} {operator} {num2} = ")

        if user_answer.isdigit() and int(user_answer) == result:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Ответ неверный")
            wrong_answers += 1

    print(f"Игра окончена. Правильных ответов: {correct_answers}")


math_game()