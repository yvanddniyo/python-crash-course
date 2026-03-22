import random


def get_choices():
    player_rock = input('Enter a choice(rock, paper, scissors: ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player": player_rock, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == 'rock' and computer == 'scissors':
        return "Rock smash scissors! You win!"
    elif player == 'rock' and computer == 'paper':
        return "Paper cover rock! you lose."
