import random

user_wins = 0
computer_wins = 0
opinions = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break
    
    if user_input not in ["rock","paper","scissors"]:
        continue
    random_number = random.randint(0,2)
    #rock is 0, paper is 1, scissors is 2
    computer_pick = opinions[random_number]
    print("Computer picked", computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
        continue
    if user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
        continue
    if user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
        continue
    if user_input == computer_pick:
        print("It's a tie!")
        continue
    else:
        print("You lost!")
        computer_wins +=1
print("You won",user_wins,"times")
print("Computer won", computer_wins,"times")
print("Goodbye")
