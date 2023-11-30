from turtle import Turtle, Screen
import random

screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen.setup(width=400, height=400)
is_race_on = False

user_answer = screen.textinput("Make Your Bet", "Which turtle will win the race? Enter a color: ").lower()
x = -100
y = -80

turtles = []
for i in range(0, 6):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x, y)
    y += 30
    turtles.append(turtle)

if user_answer:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 150:
            if turtle.pencolor() == user_answer:
                print("You have won ")
                print(f"The winner is {turtle.pencolor()} turtle")
            else:
                print("You have lost")
                print(f"The winner is {turtle.pencolor()} turtle")
            is_race_on = False
        else:
            selected_turtle = random.choice(turtles)
            step = random.randint(0, 10)
            selected_turtle.forward(step)

screen.exitonclick()
