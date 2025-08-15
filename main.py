import random

def game():
    # We have 5 choices
    choice = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']  # Choices!

    print("Welcome To The Game (Rock, Paper, Scissors, Lizard, Spock!)")
    print("If You Want To Exit, Write ('exit')!")

    # Simple Win Conditions!
    win_conditions = {
        'Rock': ['Scissors', 'Lizard'],
        'Paper': ['Rock', 'Spock'],
        'Scissors': ['Paper', 'Lizard'],
        'Lizard': ['Spock', 'Paper'],
        'Spock': ['Scissors', 'Rock']
    }
    
    while True:
        # Player Input
        you_choice = input("Enter Your Choice (Rock / Paper / Scissors / Lizard / Spock): ").capitalize()

        # Exit condition
        if you_choice == 'Exit':
            print("Exiting!")
            break
        
        # Check if input is valid
        if you_choice not in choice:
            print("Invalid Choice! Please Enter: (Rock / Paper / Scissors / Lizard / Spock)!!")
            continue

        # Computer's Choice!
        computer_choice = random.choice(choice)
        print(f"Computer's Choice: {computer_choice}")

        # Deciding the winner!
        if you_choice == computer_choice:
            print("It's a tie! Both chose the same.")
        elif computer_choice in win_conditions[you_choice]:
            print(f"Congrats! You win. {you_choice} beats {computer_choice}.")
        else:
            print(f"Computer wins! {computer_choice} beats {you_choice}.")

# Run the game
game()

'''
Game Setup:
The game has 5 choices: Rock, Paper, Scissors, Lizard, and Spock. These choices are used to play against the computer.

Player's Input:
You enter your choice (Rock, Paper, Scissors, Lizard, or Spock). You can also type 'exit' to stop the game.

Computer's Choice:
The computer randomly selects one of the 5 choices, just like you.

Game Logic:

Rock beats Scissors and Lizard.

Paper beats Rock and Spock.

Scissors beats Paper and Lizard.

Lizard beats Paper and Spock.

Spock beats Scissors and Rock.

Game Outcome:

If both you and the computer choose the same item, it's a tie.

If your choice beats the computer’s choice based on the rules, you win.

If the computer's choice beats yours, the computer wins.

Repeat or Exit:
The game continues until you type 'exit' to stop it.

'''