from random import randint
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("What number is missing in the progression?")
    count = 0
    while count < 3:

        list = gen_list(randint(0, 20), randint(1, 10))
        cor = hide_element(list, randint(0, 10))
        answer = int(input("Your answer: "))

        if answer == cor:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{cor}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def gen_list(start, step):
    i = start
    list = []
    while i <= start + 10:
        list.append(i * step)
        i += 1
    return list


def hide_element(list, index):
    res = list[index]
    list[index] = '..'
    question = 'Question: '
    for el in list:
        question += str(el) + ' '
    print(question)
    return res
