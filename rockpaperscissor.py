import random

def get_user_choice():
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter 1, 2 or 3: ")
    choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    return choices.get(choice, None)

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    
    if user == computer:
        return "It's a draw!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    user_choice = get_user_choice()
    if not user_choice:
        print("Invalid input. Try again.")
        continue

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)

    again = input("\nPlay again? (y/n): ")
    if again.lower() != 'y':
        print("Thanks for playing!")
        break
