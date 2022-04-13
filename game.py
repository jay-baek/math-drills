"""doc string placeholder"""

import random
import sys

def rand100s():
     while True:
        yield random.randint(1,100)

print(f'\n---START MATH DRILLS---'
      f'\nEnter any letter to exit'
      f'\n*Division: round to nearest hundredth')

if __name__ == "__main__":
    num = rand100s()

    pts = 0
    qNum = 1

    while True:
        a = next(rand100s())
        b = next(rand100s())

        answer = 999999
        guess = 999999

        # ch = random.choice(['add', 'sub', 'mult'])
        ch = random.choice(['add', 'sub', 'mult', 'div'])
        
        if ch == 'add':
            guess = input(f'\n{qNum}.  {a} + {b} = ')
            answer = a + b
        elif ch == 'sub':
            guess = input(f'\n{qNum}.  {a} - {b} = ')
            answer = a - b
        elif ch == 'mult':
            guess = input(f'\n{qNum}.  {a} * {b} = ')
            answer = a * b
        # DIVISION NEEDS TO BE SIMPLER
        elif ch == 'div':
            guess = input(f'\n{qNum}.  {a} / {b} = ')
            answer = round(a / b, 2) # round to nearest hundredth

        try:
            if ch == 'div':
                guess = float(guess)
            else:
                guess = int(guess)
        except ValueError:
            pts = pts - 1
            print(f'      The correct answer is {answer}.\n      Pts: {pts}')
            print(f'\nOk, see you next time. Good-bye. ^__^')
            sys.exit()

        # if guess == 'quit':
        #     print(f'The correct answer is {answer}.')
        #     print(f'\nOk, see you next time. Good-bye. ^__^')
        #     sys.exit()
        if guess == answer:
            pts = pts + 1
            print(f'      True. The correct answer is {answer}.\n      Pts: {pts}')
        else:
            pts = pts - 1
            print(f'      False. The correct answer is {answer}.\n      Pts: {pts}')
        qNum = qNum + 1

        # again = input('\nAgain? (y/n): ')
        # if again == 'y':
        #     continue
        # elif again == 'n':
        #     print('\nOk, see you next time. Good-bye.\n')
        #     sys.exit()