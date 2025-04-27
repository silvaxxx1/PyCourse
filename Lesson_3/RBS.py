import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "You win!"
        else:
            return "You lose!"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        else:
            return "You lose!"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "You win!"
        else:
            return "You lose!"

# Main function to play the game
def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")

    # User input
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return

    # Computer's random choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"The computer chose: {computer_choice}")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Play the game
rock_paper_scissors()
