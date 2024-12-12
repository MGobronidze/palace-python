import random
import time

def roll_dice():
    """Simulates rolling a six-sided die."""
    return random.randint(1, 6)

def dice_battle():
    print("🎲 Welcome to Dice Battle! 🎲")
    print("Two players compete to see who can roll the highest total score.")
    
    # Get number of rounds
    while True:
        try:
            rounds = int(input("\nHow many rounds would you like to play? "))
            if rounds <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    player1_score = 0
    player2_score = 0

    # Play rounds
    for round_num in range(1, rounds + 1):
        print(f"\n🎲 Round {round_num} 🎲")

        # Player 1's turn
        input("Player 1, press Enter to roll the dice! ")
        player1_roll = roll_dice()
        print(f"Player 1 rolled: {player1_roll}")
        player1_score += player1_roll
        print(f"Player 1's total score: {player1_score}")

        # Player 2's turn
        input("Player 2, press Enter to roll the dice! ")
        player2_roll = roll_dice()
        print(f"Player 2 rolled: {player2_roll}")
        player2_score += player2_roll
        print(f"Player 2's total score: {player2_score}")

        time.sleep(1)

    # Announce the winner
    print("\n✨ Final Scores ✨")
    print(f"Player 1: {player1_score}")
    print(f"Player 2: {player2_score}")

    if player1_score > player2_score:
        print("🎉 Player 1 wins! 🎉")
    elif player2_score > player1_score:
        print("🎉 Player 2 wins! 🎉")
    else:
        print("🤝 It's a tie! 🤝")

# Run the game
if __name__ == "__main__":
    dice_battle()
