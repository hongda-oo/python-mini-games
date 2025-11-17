import random

# A simple word list for the game
WORDS = [
    "python", "computer", "hangman", "programming", "turtle",
    "college", "student", "keyboard", "monitor", "internet"
]

max_lives = 6  # Number of wrong guesses allowed


def get_random_word():
    return random.choice(WORDS)


def display_current_state(word, guessed_letters, lives):
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
    print(f"Lives remaining: {lives}")


def get_player_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower().strip()

        # Check length
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue

        # Check if it's a letter
        if not guess.isalpha():
            print("Please enter a LETTER (a-z).")
            continue

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        return guess


def play_one_round():
    word = get_random_word()
    guessed_letters = set()
    lives = max_lives

    print("\nNew game started!")
    # Uncomment this line while testing if you want to see the word:
    # print("[DEBUG] The word is:", word)

    # Main game loop
    while True:
        display_current_state(word, guessed_letters, lives)

        # Check win: all letters guessed
        if all(letter in guessed_letters for letter in word):
            print("\n Congratulations! You guessed the word:", word)
            break

        # Check lose
        if lives <= 0:
            print("\n💀 Game over! You ran out of lives.")
            print("The word was:", word)
            break

        # Get a valid guess from the player
        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)

        # Check if guess is in the word
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            lives -= 1
            print(f"Sorry, '{guess}' is NOT in the word. You lose one life.")


def main():
    print("Welcome to Hangman!")

    while True:
        play_one_round()

        again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    main()