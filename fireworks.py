from turtle import *
import random
import math

tracer(0, 0)
speed(0)
bgcolor("black")
hideturtle()

def firework(x, y):
    penup()
    goto(x, y)
    pendown()
    color(random.random(), random.random(), random.random())
    for _ in range(60):
        forward(random.randint(50, 150))
        right(170 + random.randint(-10, 10))
        forward(5)
        right(180)
        forward(5)
        right(180)
    penup()
    goto(x, y)
    pendown()
    color("white")
    dot(10)

for _ in range(30):
    firework(random.randint(-300, 300), random.randint(-200, 400))
    update()
    delay(200)

update()
done()