from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.color('black')
        self.update_score()

    def level_up(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)