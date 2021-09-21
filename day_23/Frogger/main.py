import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard, game_over

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    game_is_on = car_manager.move_car(player.position())
    if player.ycor() >= FINISH_LINE_Y:
        player.player_reset()
        scoreboard.update_level()
        car_manager.increase_speed()
    screen.update()
game_over()

screen.exitonclick()
