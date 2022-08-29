WIN_DICTONARY = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}


def game(player_1: str, player_2: str, player_3: str):
    if player_1 == player_2 == player_3:
        return print("Tie")
    elif player_1 != player_2 != player_3:
        return print("Tie")
    #two same players
    elif player_3 and player_2 in WIN_DICTONARY[player_1]:
        return print(f"{player_1} is winner, other: Tie")
    elif player_1 and player_3 in WIN_DICTONARY[player_2]:
        return print(f"{player_2} is winner, other: Tie")
    elif player_1 and player_2 in WIN_DICTONARY[player_3]:
        return print(f"{player_3} is winner, other: Tie")
    elif player_3 and player_2 not in WIN_DICTONARY[player_1]:
        return print(f"{player_3} and {player_2} is winners, {player_1} is lose")
    elif player_1 and player_3 not in WIN_DICTONARY[player_2]:
        return print(f"{player_1} and {player_3} is winners, {player_2} is lose")
    elif player_1 and player_2 in WIN_DICTONARY[player_3]:
        return print(f"{player_1} and {player_2} is winners, {player_3} is lose")


game('rock', 'rock', 'rock')
game('rock', 'scissors', 'paper')
game('rock', 'scissors', 'scissors')
game('scissors', 'paper', 'paper')
game('rock', 'paper', 'paper')
game('paper', 'scissors', 'scissors')
