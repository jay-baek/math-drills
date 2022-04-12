"""doc string placeholder"""

import random
import sys

def rand100s():
     while True:
        yield random.randint(1,100)

if __name__ == "__main__":
    num = rand100s()

    while True:
        a = next(rand100s())
        b = next(rand100s())

        guess = input(f'\n{a} + {b} = ')

        if int(guess) == a+b:
           print(f'Well done! The correct answer is {a+b}.')
        else:
           print(f'Your answer is incorrect. The correct answer is {a+b}.')

        again = input('\nAgain? (y/n): ')
        if again == 'y':
            continue
        elif again == 'n':
            print('\nSee you next time. Good-bye.\n')
            sys.exit()