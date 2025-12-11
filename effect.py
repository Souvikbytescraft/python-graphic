from turtle import *
import math
import colorsys

speed(0)
bgcolor("dark blue")
hideturtle()
pensize(2)

for i in range(300):
    hue = (i / 100) % 1
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    color(r, g, b)
    
    forward(150)
    right(144)  # golden angle for nice symmetry
    forward(i * 0.5)
    right(72 + math.sin(i/30)*20)
    if i % 3 == 0:
        circle(20, steps=5)

update()
done()