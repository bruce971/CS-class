# Bruce diaz
# 08/01/2021
# A turtle drawing

import turtle
loadwindow=turtle.Screen()
myturtle=turtle.Turtle
turtle.color=['red','purple','blue','green','orange','yellow']
t=turtle.pen()
turtle.bgcolor('black')
for x in range (360):
    t.pencolor(turtle.color[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(60)

turtle.done()