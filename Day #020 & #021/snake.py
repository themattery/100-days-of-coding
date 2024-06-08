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
        self.snake_length = 3
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for seg in range(self.snake_length):
            self.add_segment()

    def add_segment(self, position=None):
        if position is None:
            position = (self.x_axis, self.y_axis)
            self.x_axis -= MOVE_DISTANCE
        new_turtle = Turtle('square')
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

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
