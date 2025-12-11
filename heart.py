from turtle import *
import math
import time

# Setup
tracer(0, 0)        # Fast drawing
speed(0)
bgcolor("black")
hideturtle()

# Function to draw a single heart at position (x,y) with color and size
def draw_heart(x, y, size, color_name):
    penup()
    goto(x, y)
    pendown()
    color(color_name)
    begin_fill()
    left(140)
    forward(size)
    # Left curve
    for i in range(200):
        angle = math.pi * i / 100
        dx = size * 16 * math.sin(angle)**3
        dy = size * (13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle))
        goto(x + dx * 0.8, y + dy * 0.8 - size*5)
    goto(x, y - size*12)
    # Right curve
    left(80)
    for i in range(200):
        angle = math.pi * i / 100
        dx = size * 16 * math.sin(angle)**3
        dy = size * (13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle))
        goto(x + dx * 0.8, y + dy * 0.8 - size*5)
    end_fill()
    right(220)  # reset direction

# Clear screen
clear()

# Draw girl's heart (pink) on the left
draw_heart(-150, 50, 10, "#ff69b4")  # Hot pink

# Draw boy's heart (blue) on the right
draw_heart(150, 50, 10, "#4169e1")   # Royal blue

update()
time.sleep(2)

# Animation: hearts move towards each other and merge
for step in range(50):
    clear()
    offset = 150 - step * 6  # move closer
    
    # Girl heart moves right
    draw_heart(-offset, 50 + math.sin(step*0.3)*10, 10 + step*0.15, "#ff69b4")
    # Boy heart moves left
    draw_heart(offset, 50 + math.sin(step*0.3 + 1)*10, 10 + step*0.15, "#4169e1")
    
    update()
    time.sleep(0.05)

# Final merged big heart (purple = love combination)
clear()
draw_heart(0, 50, 18, "#c71585")  # Deep purple-pink
draw_heart(0, 50, 18, "#ff1493")  # Bright magenta outline
color("white")
penup()
goto(0, -100)
write("Together Forever ♡", align="center", font=("Arial", 28, "bold"))

# Little beating effect
for i in range(8):
    clear()
    scale = 18 + math.sin(i)*2
    draw_heart(0, 50, scale, "#ff1493")
    draw_heart(0, 50, scale-2, "#c71585")
    penup()
    goto(0, -100)
    write("Together Forever ♡", align="center", font=("Arial", 28, "bold"))
    update()
    time.sleep(0.3)

update()
done()