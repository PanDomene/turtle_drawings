from turtle import Turtle, Screen
import random

pia = Turtle()
pia.shape('turtle')

# Draw polygons


def draw_figure(no_of_sides):
    angle = 360/no_of_sides
    for side in range(no_of_sides):
        pia.forward(100)
        pia.right(angle)


# for polygon in range(3, 11):
#     pia.color((random.random(), random.random(), random.random()))
#     draw_figure(polygon)


# Random Walk

# turn = [0, 90, 180, -90]
# pia.pensize(10)
# pia.speed(0)
#
# for _ in range(200):
#     pia.color((random.random(), random.random(), random.random()))
#     pia.setheading(random.choice(turn))
#     pia.forward(25)


# Spirograph

pia.speed(0)


def spyrograph(rad, num_of_circles):
    for i in range(num_of_circles+1):
        pia.color((random.random(), random.random(), random.random()))
        pia.circle(rad)
        pia.right(360/num_of_circles)


pia.pensize(2)
for radius in range(30, 91, 30):
    spyrograph(radius, 70)

spyrograph(100, 150)

screen = Screen()
screen.exitonclick()
