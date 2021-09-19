from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for num in range(0, 3):
            s = Turtle(shape="square")
            s.penup()
            s.color("white")
            s.setposition((-20 * num), 0)
            self.snake.append(s)

    def move(self):
        for s in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[s - 1].xcor()
            new_y = self.snake[s - 1].ycor()
            self.snake[s].goto(new_x, new_y)

        self.head.forward(20)

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
