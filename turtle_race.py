import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("lightblue")
screen.setup(width=800, height=400)

# Ask the user to bet on a turtle color 
colors = ["red", "blue", "green", "orange", "purple", "yellow"]

print("\nAvailable turtles:", ", ".join(colors))
user_bet = input("Which turtle will win the race? Type a color: ").lower()

# Draw finish line
finish_line = 350

line = turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(finish_line, -150)
line.left(90)
line.pensize(3)

# Draw dashed finish line
for _ in range(15):
    line.forward(20)
    line.penup()
    line.forward(10)
    line.pendown()

# Create turtles
turtles = []
start_x = -350
start_y = -120

for index, color in enumerate(colors):
    racer = turtle.Turtle(shape="turtle")
    racer.color(color)
    racer.penup()
    racer.goto(start_x, start_y + index * 50)
    turtles.append(racer)

race_on = False

# Only start the race if the user placed a bet
if user_bet:
    race_on = True

# Main race loop
while race_on:
    for racer in turtles:
        # Move each turtle a random distance
        distance = random.randint(1, 10)
        racer.forward(distance)

        # Check if a turtle has crossed the finish line
        if racer.xcor() >= finish_line:
            race_on = False
            winning_color = racer.pencolor()

            if user_bet == winning_color:
                print(f"\n You WIN! The {winning_color} turtle is the champion! ")
            else:
                print(f"\n You lost. The {winning_color} turtle won the race.")
            break

# Keep the window open until clicked
screen.exitonclick()