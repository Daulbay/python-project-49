import random
from random import randint
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count < 3:
        num = randint(1,100)
        print(f"Question:{num}")

        answer = input('Your answer: ')

        correctAns = 'yes' if num % 2 == 0 else 'no'

        if answer == correctAns:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correctAns}'.")
            print(f"Let's try again, {name}!")
            return
        
        count += 1
    print(f'Congratulations, {name}!')