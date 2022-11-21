import turtle
from turtle import Turtle,Screen
import random as rm
tim = Turtle()


turtle.colormode(255)

def random_colour():
    r=rm.randint(0, 255)
    g = rm.randint(0, 255)
    b = rm.randint(0, 255)
    return (r,g,b)


dir=[0,90,270,180]
tim.pensize(10)
tim.speed("fastest")
for i in range(200):
    angle = rm.choice(dir)
    tim.pencolor(random_colour())
    tim.setheading(angle)
    tim.forward(20)








screen = Screen()
screen.exitonclick()