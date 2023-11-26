from random import randint
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("What is the result of the expression?")
    count = 0
    while count < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        cor = get_ans(a, b, count)
        str = input("Your answer: ")
        ans = int(str)
        if ans == cor:
            print("Correct!")
            count += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def get_ans(a, b, op):
    if op == 0:
        print(f'Question: {a} + {b}')
        return a + b
    elif op == 1:
        print(f'Question: {a} - {b}')
        return a - b
    else:
        print(f'Question: {a} * {b}')
        return a * b
