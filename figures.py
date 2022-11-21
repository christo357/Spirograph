from turtle import Turtle,Screen
import random as rm
tim = Turtle()


clr=["red","black","blue","yellow","green","violet","indigo"]

for i in range(3,11):
    colour = rm.choice(clr)
    for j in range(i):

        tim.pencolor(colour)
        tim.forward(50)
        tim.left(360/i)

screen = Screen()
screen.exitonclick()