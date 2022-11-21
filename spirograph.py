import turtle
from turtle import Turtle,Screen
import random as rm
tim = Turtle()
tim.speed(0)


turtle.colormode(255)
def rand_colour():
    r=rm.randint(0,255)
    y = rm.randint(0, 255)
    b = rm.randint(0, 255)
    return (r,y,b)

def draw_spirograph(size_of_gap):
    for i in range(360//size_of_gap):
        tim.pencolor(rand_colour())

        tim.circle(100)
        cur_heading = tim.heading()
        tim.setheading(cur_heading + size_of_gap)




draw_spirograph(1)
screen = Screen()
screen.exitonclick()
