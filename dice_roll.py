import random

# Function: roll a 6-sided die
def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Ask how many players will play
while True:
    players = input("Enter the number of players (1-4): ")

    # Check if it's a number
    if players.isdigit():
        players = int(players)

        # Check range
        if 1 <= players <= 4:
            break
        else:
            print("Number of players must be between 1 and 4.")
    else:
        print("Invalid input. Please type a number.")

# Set the maximum score needed to win
max_score = 50

# Create a score list for all players initialized to 0
player_scores = [0 for _ in range(players)]

print("\nStarting game with", players, "players!")
print("First player to reach", max_score, "points wins!\n")

# Game loop
while max(player_scores) < max_score:
    for player_idx in range(players):
        input(f"Player {player_idx + 1}, press Enter to roll the dice...")
        roll_value = roll()
        print(f"Player {player_idx + 1} rolled a {roll_value}!")

        # Add roll value to player's score
        player_scores[player_idx] += roll_value
        print(f"Player {player_idx + 1}'s total score is now {player_scores[player_idx]}\n")

        # Check if this player reached the winning score
        if player_scores[player_idx] >= max_score:
            break

# Find the winner
winner = player_scores.index(max(player_scores)) + 1
print(f" Player {winner} wins with {player_scores[winner - 1]} points! ")