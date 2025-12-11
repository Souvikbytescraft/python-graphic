from turtle import *
from colorsys import hsv_to_rgb
import math

# Ultra-fast rendering
tracer(0, 0)          # Turn off animation (huge speed boost)
speed(0)
bgcolor("black")
hideturtle()

# Parameters for beauty & performance
steps = 360 * 8       # More steps = smoother (2880 total)
radius = 150
hue = 0.0

# Pre-calculate for maximum speed
for i in range(steps):
    hue = i / steps                     # Smooth hue cycle (0 to 1)
    r, g, b = hsv_to_rgb(hue, 1, 1)     # Full saturation & brightness
    color(r, g, b)
    
    # Create flowing spiral with perfect curvature
    forward(i * 0.07)       # Increasing step size for spiral growth
    right(59)               # Magic angle for beautiful non-repeating pattern
    right(math.sin(i / 20) * 2)  # Subtle wave for organic feel

# Final update to show everything at once
update()
done()