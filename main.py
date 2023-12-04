# Welcome to Turtle Race. Created by Dwi Didit Prasetiyo

from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=600, height=600)

user_input = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []

for turtle_index in range(0, 6):
    new_tim = Turtle()
    new_tim.shape("turtle")
    new_tim.penup()
    new_tim.goto(x=-280, y=-100 + turtle_index * 40)
    new_tim.color(colors[turtle_index])
    all_turtles.append(new_tim)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                screen.title(f"You've won! The {winning_color} turtle is the winner!")

            else:
                screen.title(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)







screen.exitonclick()
