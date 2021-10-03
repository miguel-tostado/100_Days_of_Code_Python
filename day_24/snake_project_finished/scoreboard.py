from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")
FILE = "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto((0, 268))
        self.score = 0
        with open(FILE) as data:
            self.high_score = int(data.read())
        self.write_score()

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
