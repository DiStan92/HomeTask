from random import randint

TOOLS = ['rock', 'scissors', 'paper']
WIN_DICTONARY = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}


def game(player_1: str, player_2: str, player_3: str):
    print(player_1, player_2, player_3)
    different_player = list(set([player_1, player_2, player_3]))
    if len(different_player) == 1 or len(different_player) == 3:
        print("Tie")
        return game(*gen_players())
    elif player_1 == player_2 and player_1 in WIN_DICTONARY[player_3]:
        return print(f'player_3 {player_3} is winner')
    elif player_1 == player_3 and player_3 in WIN_DICTONARY[player_2]:
        return print(f'player_2 {player_2} is winner')
    elif player_3 == player_2 and player_3 in WIN_DICTONARY[player_1]:
        return print(f'player_1 {player_1} is winner')
    else:
        return game_2(*gen_player_new())


def game_2(player_1, player_2):
    print(player_1, player_2)
    if player_1 == player_2:
        print('Tie')
        return game_2(*gen_player_new())
    elif player_1 in WIN_DICTONARY[player_2]:
        return print(f'player_2 {player_2} is winner')
    else:
        return print(f'player_1 {player_1} is winner')


def gen_players():
    res = [TOOLS[randint(0, 2)] for _ in range(3)]
    return res


def gen_player_new():
    res = [TOOLS[randint(0, 2)] for _ in range(2)]
    return res


game(*gen_players())

