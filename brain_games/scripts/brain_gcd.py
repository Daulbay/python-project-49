from random import randint
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f'Question: {a} {b}')
        cor = get_ans(a, b)
        str = input("Your answer: ")
        answer = int(str)
        if answer == cor:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{cor}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def get_ans(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b
