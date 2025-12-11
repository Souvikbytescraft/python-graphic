from turtle import *
from colorsys import hsv_to_rgb
import math

# Optimized Turtle Setup
tracer(0, 0)
speed(0)
bgcolor("black")
hideturtle()
pensize(2)

# Improved: smoother color cycle, dynamic angle, and spiral variation
for i in range(1000):
    hue = (i / 300) % 1   # faster color cycling
    r, g, b = hsv_to_rgb(hue, 1, 1)
    color(r, g, b)

    forward(math.sqrt(i))  # smoother exponential spiral

    # Dynamic rotation design
    base_angle = 61
    wave = math.sin(i / 15) * 20

    if i % 2 == 0:
        left(base_angle + wave)
    else:
        right(base_angle + wave)

update()
done()