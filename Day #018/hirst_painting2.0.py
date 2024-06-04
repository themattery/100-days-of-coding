import turtle as t
import random

t.colormode(255)
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85)]
tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.fd(300)
tim.setheading(0)

dots_amount = 100

for dot_count in range(1, dots_amount + 1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
