# -*- coding: utf-8 -*-

from bullsandcows_engine import generate_number, check_number
from termcolor import cprint, colored

while True:
    turn = 0
    generate_number()
    cprint('The number is guessed! '
           'The number consists of 4 non-repeating digits.',
           'yellow')
    while True:
        user_input = input(colored('Enter your number: ', 'blue'))
        cprint(user_input, 'cyan')
        result = check_number(user_input)
        if result is None:
            cprint('According to the rules, you must enter a four-digit number'
                   'with non-repeating digits!', 'red')
        else:
            cprint(f'> bulls - {result["bulls"]}, cows - {result["cows"]}',
                   'magenta')
            turn += 1
            if result['bulls'] == 4:
                break
    if result['bulls'] == 4:
        cprint('You have won!', 'green')
        cprint(f'Number of moves - {turn}', 'green')
        cprint('Do you want to play again?', 'green')
        break
