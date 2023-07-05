import random

choices = ("rock", "paper", "scissor")
running = True

while running:
    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("Your Choice: ")

    
    print(f"Player Choice  : {player}")
    print(f"Computer Choice: {computer}")

    if player == computer:
        print("Tie")
    elif player == "rock" and computer == "scissor":
        print("You Win")
    elif player == "paper" and computer == "rock":
        print("You Win")
    elif player == "scissor" and computer == "paper":
        print("You Win")
    else:
        print("You Lose")

    print()

    if not input("Play Again? (y/n): ").lower() == "y":
        running = False
        print("Thank you for playing")