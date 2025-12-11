from turtle import *
import random

speed(0)
bgcolor("black")
hideturtle()
color("lime")

def tree(length, depth):
    if depth == 0:
        return
    forward(length)
    left(30)
    tree(length * 0.7, depth - 1)
    right(60)
    tree(length * 0.7, depth - 1)
    left(30)
    backward(length)

penup()
goto(0, -200)
pendown()
left(90)
tree(150, 10)

update()
done()