from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

l_score = Scoreboard((-100, 240))
r_score = Scoreboard((100, 240))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with either paddle
    if ball.xcor() == 330 or ball.xcor() == -330:
        if ball.distance(r_paddle) <= 50 or ball.distance(l_paddle) <= 50:
            ball.bounce_x()
    elif ball.xcor() > 380:
        l_score.update_score()
        ball.reset()
    elif ball.xcor() < -380:
        r_score.update_score()
        ball.reset()


screen.exitonclick()
