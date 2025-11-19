import random

print("Welcome to the Coin Flip Game!")

wins = 0
losses = 0

while True:
    # Ask player to guess
    guess = input("\nGuess the coin flip: (h)eads, (t)ails or (q)uit: ").lower().strip()

    # Handle quit
    if guess == "q":
        break

    # Input validation
    if guess not in ["h", "t", "heads", "tails"]:
        print("Invalid choice. Please type h, t, or q.")
        continue

    # Normalize guess to "heads" or "tails"
    if guess == "h":
        guess = "heads"
    elif guess == "t":
        guess = "tails"

    # Randomly choose coin side
    result = random.choice(["heads", "tails"])
    print("The coin landed on:", result)

    # Compare guess with result
    if guess == result:
        print("You guessed right! ")
        wins += 1
    else:
        print("You guessed wrong.")
        losses += 1

    print(f"Score → Wins: {wins}, Losses: {losses}")

print("\nGame over.")
print(f"Final score → Wins: {wins}, Losses: {losses}")
print("Goodbye!")