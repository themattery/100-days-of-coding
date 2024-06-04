import turtle as t
import random as r

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85)]
screen = t.Screen()
screen.colormode(255)
tim = t.Turtle()
tim.up()
tim.bk(200)


def draw_dot():
    for _ in range(10):
        tim.down()
        color = r.choice(color_list)
        tim.dot(20, color)
        tim.up()
        tim.fd(50)


def draw_painting():
    for _ in range(10):
        draw_dot()
        tim.up()
        tim.left(90)
        tim.fd(50)
        tim.left(90)
        tim.fd(50*10)
        tim.left(180)


draw_painting()
screen.exitonclick()
