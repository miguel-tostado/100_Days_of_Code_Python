from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(position)
        self.write_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write(arg=f"{self.score}", font=("Ariel", 35, "normal"))
