from turtle import *
from colorsys import hsv_to_rgb
import math

tracer(0,0)
speed(0)
bgcolor("black")
hideturtle()
pensize(2)

for i in range(4000):
    hue = (i * 0.618033988749) % 1  # Golden ratio for perfect color distribution
    color(hsv_to_rgb(hue, 1, 1))
    forward(i * 0.05)
    right(91 + math.sin(i/30)*5)   # Chaos + harmony
    right(0.1)  # Tiny drift

update()
done()