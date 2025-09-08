import random

choices = ("rock", "paper", "scissors")

def player_input():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in choices:
            return choice
        print("Invalid choice. Please try again.")

def computer_input():
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    wins = (player == "rock" and computer == "scissors") or \
           (player == "paper" and computer == "rock") or \
           (player == "scissors" and computer == "paper")
    return "You win!" if wins else "Computer wins!"

def play_game():
    player_choice = player_input()
    computer_choice = computer_input()
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(player_choice, computer_choice))

play_game()
