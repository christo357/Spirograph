import turtle
from turtle import Turtle,Screen
import colorgram as cg
import random as rm
tim = Turtle()
tim.speed("fastest")

#clr=["red","black","blue","yellow","green","violet","indigo"]
turtle.colormode(255)
tim.hideturtle()
tim.penup()
tim.goto(x=-200,y=-200)



def rand_colour():
    rgb_colours = []
    colours = cg.extract("image.jfif", 30)
    for colour in colours:
        r = colour.rgb.r
        b = colour.rgb.b
        g = colour.rgb.g
        new_color = (r, g, b)
        rgb_colours.append(new_color)
    return rm.choice(rgb_colours)

def line_dot(n, r):
    for i in range(n):
        tim.dot(r,rand_colour())
        tim.forward(50)

def draw_heist(n,r):
    for i in range(n):
        line_dot(n, r)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(50*n)
        tim.setheading(0)



draw_heist(10,20)
screen = Screen()
screen.exitonclick()
