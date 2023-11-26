from random import randint
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 0
    while count < 3:
        num = randint(1, 100)
        print(f"Question: {num}")
        ans = input('Your answer: ')
        cor = is_prime(num)
        if ans == cor:
            print('Correct!')
            count += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def is_prime(x):
    for i in range(2, x - 1):
        if x % i == 0:
            return ("no")
    return ("yes")
