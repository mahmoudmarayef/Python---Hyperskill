import random
player = ['John', 'Jack']
bot_move = random.randint(1, 3)


def check_num():
    num = input('How many pencils would you like to use')
    while True:
        try:
            num = int(num)
            if num == 0:
                num = input('The number of pencils should be positive')
                continue
            elif num < 0:
                raise ValueError
            else:
                return num
        except ValueError:
            num = input('The number of pencils should be numeric')
            continue


def go_first():
    v1 = input(f'Who will be the first ({player[0]}, {player[1]}):')
    while v1 not in player:
        v1 = input(f"Choose between '{player[0]}' and '{player[1]}'")
    print('|' * pencils)
    return v1


def go_second(v1):
    if v1 == player[0]:
        return player[1]
    else:
        return player[0]


def bot(v3):
    if v3 in range(5, v3 + 1, 4):
        return bot_move
    elif v3 == 1:
        return 1
    elif v3 in range(2, v3 + 1, 4):
        return 1
    elif v3 in range(3, v3 + 1, 4):
        return 2
    elif v3 in range(4, v3 + 1, 4):
        return 3


def possible_value(v1):
    take = input(f"{v1}'s turn:")
    while True:
        try:
            take = int(take)
            if take not in [1, 2, 3]:
                take = input("Possible values: '1', '2', '3'")
                continue
            else:
                break
        except ValueError:
            take = input("Possible values: '1', '2', '3'")
            continue
    return take


def too_many(take, v3):
    while take > v3:
        take = int(input('Too many pencils were taken'))
    return take


def take_turn(v1, v2, v3):
    # Who start?
    if v1 == player[0]:  # If player goes first
        i = 0
    else:  # If bot goes first
        i = 1
        temp = v2
        v2 = v1
        v1 = temp
    # Alternate
    while v3 > 0:
        if i % 2 == 0:
            take = possible_value(v1)
            take = too_many(take, v3)
            v3 -= take
            print('|' * v3)
            i += 1
            if v3 == 0:
                return v2
        else:
            take = bot(v3)
            print(f"{v2}'s turn:")
            print(take)
            v3 -= take
            print('|' * v3)
            i += 1
    else:
        return v1


def pick_winner():
    print(f"{winner} won!")


while True:
    pencils = check_num()
    first = go_first()
    second = go_second(first)
    winner = take_turn(first, second, pencils)
    pick_winner()
    break