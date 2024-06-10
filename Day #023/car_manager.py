from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car_ycor = random.randint(-245, 245)
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, car_ycor)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.setx(car.xcor() - self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
