"""doc string placeholder"""

import random
import sys

def rand10s():
     while True:
        yield random.randint(1,10)

def rand100s():
     while True:
        yield random.randint(1,100)

def rand1000s():
     while True:
        yield random.randint(1,100)


print(f'\n---START MATH DRILLS---'
      f'\nEnter any letter to exit'
      f'\n*Division: round to nearest hundredth')

if __name__ == "__main__":

    level, pts, qNum = 1, 0, 1

    def set_level(points):
        global level
        if points > 20:
            level = 3
        elif points > 10:
            level = 2
        elif points <= 10:
            level = 1
        elif points < 0:
            level = 0

    def equation(factor_a, factor_b, type: str):
        if type == 'add':
            guess = input(f'\n{qNum}.  {factor_a} + {factor_b} = ')
            answer = factor_a + factor_b
            return guess, answer
        if type == 'sub':
            guess = input(f'\n{qNum}.  {factor_a} - {factor_b} = ')
            answer = factor_a - factor_b
            return guess, answer
        if type == 'mult':
            guess = input(f'\n{qNum}.  {factor_a} * {factor_b} = ')
            answer = factor_a * factor_b
            return guess, answer
        if type == 'div':
            guess = input(f'\n{qNum}.  {factor_a} / {factor_b} = ')
            answer = round(factor_a / factor_b, 2) # round to nearest hundredth
            return guess, answer

    while True:
        b10 = next(rand10s())
        a100 = next(rand100s())
        b100 = next(rand100s())
        a1000 = next(rand1000s())

        answer, guess = 999999, 999999

        ch = random.choice(['add', 'sub', 'mult', 'div'])


        if level == 1:
            guess, answer = equation(a100, b10, ch)
        if level == 2:
            guess, answer = equation(a100, b100, ch)
        if level == 3:
            guess, answer = equation(a1000, b100, ch)

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
            set_level(pts)
            print(f'      True. The correct answer is {answer}.\n      Pts: {pts}   Lvl: {level}')
        else:
            pts = pts - 1
            set_level(pts)
            print(f'      False. The correct answer is {answer}.\n      Pts: {pts}   Lvl: {level}')
        qNum = qNum + 1

        # again = input('\nAgain? (y/n): ')
        # if again == 'y':
        #     continue
        # elif again == 'n':
        #     print('\nOk, see you next time. Good-bye.\n')
        #     sys.exit()