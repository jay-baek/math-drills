"""doc string placeholder"""

import random
import sys

def rand10s():
     while True:
        yield random.randint(1,10)

def rand100s():
     while True:
        yield random.randint(1,100)

print(f'\n---START MATH DRILLS---'
      f'\nEnter any letter to exit'
      f'\n*Division: round to nearest hundredth')

if __name__ == "__main__":

    level = 1
    pts = 0
    qNum = 1

    while True:
        b10 = next(rand10s())
        a100 = next(rand100s())
        b100 = next(rand100s())

        answer = 999999
        guess = 999999

        # ch = random.choice(['add', 'sub', 'mult'])
        ch = random.choice(['add', 'sub', 'mult', 'div'])

        if pts < 10:
            level = 1
        if pts > 10:
            level = 2

        if level == 1:
            if ch == 'add':
                guess = input(f'\n{qNum}.  {a100} + {b10} = ')
                answer = a100 + b10
            elif ch == 'sub':
                guess = input(f'\n{qNum}.  {a100} - {b10} = ')
                answer = a100 - b10
            elif ch == 'mult':
                guess = input(f'\n{qNum}.  {a100} * {b10} = ')
                answer = a100 * b10
            elif ch == 'div':
                guess = input(f'\n{qNum}.  {a100} / {b10} = ')
                answer = round(a100 / b10, 2) # round to nearest hundredth

        if level == 2:
            if ch == 'add':
                guess = input(f'\n{qNum}.  {a100} + {b100} = ')
                answer = a100 + b100
            elif ch == 'sub':
                guess = input(f'\n{qNum}.  {a100} - {b100} = ')
                answer = a100 - b100
            elif ch == 'mult':
                guess = input(f'\n{qNum}.  {a100} * {b100} = ')
                answer = a100 * b100
            elif ch == 'div':
                guess = input(f'\n{qNum}.  {a100} / {b100} = ')
                answer = round(a100 / b100, 2) # round to nearest hundredth

        try:
            if ch == 'div':
                guess = float(guess)
            else:
                guess = int(guess)
        except Exception as e:
            print(f'    Error: {e}')
            quit = input(f'    Do you want to quit (y/n)?  ')
            if quit == 'n':
                continue
            elif quit == 'y' or quit == '':
                pts = pts - 1
                print(f'      The correct answer is {answer}.\n      Pts: {pts}   Lvl: {level}')
                print(f'\nOk, see you next time. Good-bye. ^__^')
                sys.exit()

        if guess == answer:
            pts = pts + 1
            print(f'      True. The correct answer is {answer}.\n      Pts: {pts}   Lvl: {level}')
        else:
            pts = pts - 1
            print(f'      False. The correct answer is {answer}.\n      Pts: {pts}   Lvl: {level}')
        qNum = qNum + 1

        # again = input('\nAgain? (y/n): ')
        # if again == 'y':
        #     continue
        # elif again == 'n':
        #     print('\nOk, see you next time. Good-bye.\n')
        #     sys.exit()