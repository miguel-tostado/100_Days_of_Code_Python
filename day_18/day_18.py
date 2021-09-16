from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

screen = Screen()
screen.colormode(255)

for _ in range(4):
    tim.forward(100)
    tim.right(90)

tim.forward(100)
for _ in range(50):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for side in range(3, 11):
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw_shape(side)

tim.pensize(15)
tim.speed("fastest")

directions = [0, 90, 180, 270]

for walk in range(0):
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.setheading(random.choice(directions))
    tim.forward(30)

divisor = 52
angle = 360 / divisor
count = 0

while count < divisor:
    count += 1
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.circle(100)
    tim.setheading(angle * count)

screen.exitonclick()
