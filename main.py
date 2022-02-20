import turtle
from turtle import Turtle, Screen
import random

direction = [0, 90, 180, 270]

t = Turtle()
s = Screen()
s.bgcolor('black')
t.pensize(10)
t.speed('fastest')
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(500):
    t.setheading(random.choice(direction))
    t.forward(20)
    t.color(random_color())

s.exitonclick()
