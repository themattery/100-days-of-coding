from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def create_turtles():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    turtles = []
    x_axis = -230
    y_axis = -100
    for _ in range(0, 6):
        turtles.append(Turtle(shape="turtle"))
        turtles[_].penup()
        turtles[_].color(colors[_])
        turtles[_].goto(x=x_axis, y=y_axis)
        y_axis += 40
    return turtles


def start_game():
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    turtles = create_turtles()
    race_on = False

    if user_bet:
        race_on = True

    while race_on:
        turtle = random.choice(turtles)
        if turtle.xcor() > 230:
            race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You won! {winner_color.title()} turtle won!")
            else:
                print(f"You lose! {winner_color.title()} turtle won.")
        distance = random.randint(0, 10)
        turtle.fd(distance)


start_game()
screen.exitonclick()
