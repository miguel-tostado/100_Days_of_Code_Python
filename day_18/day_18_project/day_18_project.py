from turtle import Turtle, Screen
import random

# import colorgram

# colors = colorgram.extract("./hirst.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [
    (249, 248, 248),
    (237, 241, 245),
    (238, 246, 244),
    (249, 243, 247),
    (1, 12, 31),
    (53, 25, 17),
    (218, 127, 106),
    (10, 104, 159),
    (242, 213, 68),
    (149, 83, 39),
    (215, 87, 63),
    (155, 6, 24),
    (165, 162, 31),
    (157, 62, 102),
    (10, 64, 33),
    (206, 74, 104),
    (11, 96, 57),
    (95, 6, 20),
    (174, 135, 163),
    (1, 61, 145),
    (7, 172, 216),
    (3, 213, 207),
    (159, 33, 24),
    (8, 140, 85),
    (145, 227, 217),
    (122, 193, 147),
    (220, 177, 216),
    (100, 218, 229),
    (117, 171, 192),
    (79, 135, 178),
]

t = Turtle()
t.penup()
t.speed("fastest")

screen = Screen()
screen.colormode(255)


def dot(color):
    t.dot(20, color)


x = -250
y = -250

t.setposition(x, y)

while y < 250:
    while x < 250:
        color = random.choice(color_list)
        dot(color)
        x += 50
        if x < 250:
            t.forward(50)
    x = -250
    y += 50
    if y < 250:
        t.setposition(x, y)


screen.exitonclick()
