from turtle import Turtle

FONT = ("Courier", 24, "normal")


def game_over():
    message = Turtle()
    message.write("GAME OVER", align="center", font=FONT)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.write_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write_level()

    def write_level(self):
        self.write(f"Level: {self.level}", font=FONT)
