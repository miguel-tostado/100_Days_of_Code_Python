from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def new_coords():
    new_coord = (random.randint(310, 910), random.randint(-260, 280))
    return new_coord


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()

    def create_cars(self):
        for i in range(20):
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2)
            car.setheading(180)
            car.penup()
            car.move_speed = STARTING_MOVE_DISTANCE
            car.goto(new_coords())
            self.cars.append(car)

    def move_car(self, player):
        for car in self.cars:
            if car.ycor() - 20 < player[1] < car.ycor() + 20:
                if car.xcor() - 30 < player[0] < car.xcor() + 30:
                    return False

            if car.xcor() < -310:
                car.goto(new_coords())
            else:
                car.forward(car.move_speed)
        return True

    def increase_speed(self):
        for car in self.cars:
            car.move_speed += MOVE_INCREMENT
