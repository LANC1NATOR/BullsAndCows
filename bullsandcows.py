# -*- coding: utf-8 -*-

from bullsandcows_engine import generate_number, check_number
from termcolor import cprint, colored

while True:
    turn = 0
    generate_number()
    cprint('Число загадано! Число состоит из 4 неповторяющихся цифр.',
           'yellow')
    while True:
        user_input = input(colored('Введите Ваше число: ', 'blue'))
        cprint(user_input, 'cyan')
        result = check_number(user_input)
        if result is None:
            cprint('По правилам необходимо ввести четырехзначное число c '
                   'неповторяющимися цифрами!', 'red')
        else:
            cprint(f'> быки - {result["bulls"]}, коровы - {result["cows"]}',
                   'magenta')
            turn += 1
            if result['bulls'] == 4:
                break
    if result['bulls'] == 4:
        cprint('Вы выиграли!', 'green')
        cprint(f'Количество ходов - {turn}', 'green')
        cprint('Хотите еще партию?', 'green')
        break
