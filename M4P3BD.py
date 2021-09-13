#Bruce Diaz
#This program will as for number of sides length adn color and then draw polygon

from turtle import Turtle, lt, pencolor, speed, 
speed(10)
sides=int(input("enter the number of sides:"))
Length=int(input("enter the length:"))
color=input("enter the color")
pencolor(color)
for i in range(sides):
    forward(Length)
    lt(360/sides)
    