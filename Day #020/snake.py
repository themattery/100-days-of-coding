from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.x_axis = 0
        self.y_axis = 0
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for _ in range(3):
            position = (self.x_axis, self.y_axis)
            self.turtles.append(Turtle('square'))
            self.turtles[_].penup()
            self.turtles[_].color('white')
            self.turtles[_].goto(position)
            self.x_axis -= MOVE_DISTANCE

    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle - 1].xcor()
            new_y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)