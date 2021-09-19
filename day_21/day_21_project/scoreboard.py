from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto((0, 268))
        self.score = 0
        self.write_score()

    def add_point(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
