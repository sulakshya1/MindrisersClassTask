
import random

print("=" * 35)
print("     ROCK, PAPER, SCISSORS")
print("=" * 35)

player_score = 0
computer_score = 0

while True:
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Try again.")
        continue

    moves = {
        "1": "rock",
        "2": "paper",
        "3": "scissors"
    }

    player = moves[choice]
    computer = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"\nYour score: {player_score}")
    print(f"Computer score: {computer_score}")

print("\n========== FINAL SCORE ==========")
print(f"Your score: {player_score}")
print(f"Computer score: {computer_score}")

if player_score > computer_score:
    print("Congratulations! You won the game!")
elif computer_score > player_score:
    print("Computer won the game. Better luck next time!")
else:
    print("The game ended in a tie!")

print("Thanks for playing!")
