from turtle import *
import colorsys

speed(0)
bgcolor("black")
hideturtle()
pensize(3)

def draw_circle(x, y, radius, hue):
    penup()
    goto(x, y - radius)
    pendown()
    color(colorsys.hsv_to_rgb(hue, 1, 1))
    circle(radius)

for i in range(36):
    hue = i / 36
    for r in range(50, 250, 30):
        draw_circle(0, 0, r, hue)
    left(10)

update()
done()