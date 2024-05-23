from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput("Your Bet", "Which turtle will win the race? Enter a Color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet", "indigo"]
y_position = [-120, -80, -40, 0, 40, 80, 120]
turtles = []

if user_bet:
    race_on = True

for turtle_index in range(7):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-380, y=y_position[turtle_index])
    turtles.append(turtle)

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 380:
            race_on = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_bet:
                print(f"You won!, The {winner_turtle} turtle is won the race!")
            else:
                print(f"You lost!, The {winner_turtle} turtle is won the race!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

