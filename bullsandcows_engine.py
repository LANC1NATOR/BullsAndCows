from random import randint

_number = []


def generate_number():
    global _number
    _number = []
    unique_number = []
    for i in range(4):
        if i == 0:
            _number.append(randint(1, 9))
        else:
            _number.append(randint(0, 9))
    for number in _number:
        if number not in unique_number:
            unique_number.append(number)
    while len(_number) > len(unique_number):
        random_number = (randint(0, 9))
        if random_number not in unique_number:
            unique_number.append(random_number)
    _number = unique_number
    return _number


def check_number(user_number):
    bulls_and_cows = {'bulls': 0, 'cows': 0}
    check_for_correct_input = user_number.isdigit() and len(user_number) == \
                              len(_number)
    if check_for_correct_input is True:
        user_number_list = list(user_number)
        user_number_list = list(map(int, user_number_list))
        unique_number = []
        for number in user_number_list:
            if number not in unique_number:
                unique_number.append(number)
        if unique_number == user_number_list:
            for number in user_number_list:
                if number in _number and user_number_list.index(number) == \
                        _number.index(number):
                    bulls_and_cows['bulls'] += 1
                elif number in _number and user_number_list.index(number) != \
                        _number.index(number):
                    bulls_and_cows['cows'] += 1
            return bulls_and_cows
        else:
            return None
    else:
        return None
