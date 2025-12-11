from turtle import *
import math
import colorsys
import random
import time

# ULTRA SMOOTH & STABLE SETUP
tracer(0, 0)
speed(0)
bgcolor("black")
hideturtle()
colormode(255)
title("HAPPY BIRTHDAY AVIK - 3D ULTIMATE EDITION 2025")

# Safe 3D Projection
def project(x, y, z=0, scale=1.3, dist=700):
    f = dist / (dist + z + 150)
    return x * f * scale, y * f * scale + 100

# Dynamic Neon Glow
def glow(t, offset=0):
    h = (time.time() * 0.6 + t + offset) % 1
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
    return int(r*255), int(g*255), int(b*255)

# 3D Rotating Cake with Depth & Beauty
def draw_cake(angle):
    layers = [
        (120, 55, (160,82,45), (205,133,63)),
        (95, 40, (255,105,180), (255,192,203)),
        (70, 30, (100,200,255), (173,216,230))
    ]
    
    # Draw depth layers (back to front)
    for depth in range(15):
        for i, (w, h, col1, col2) in enumerate(layers):
            z = i * 38 + depth * 6
            y_base = -150 + z
            
            # Darker sides for 3D effect
            r,g,b = col1
            shade = max(30, 255 - depth * 18)
            color(min(r + depth*8, 255), g//(1 + depth//5), b//(1 + depth//5))
            penup()
            x1, y1 = project(-w/2, y_base, z)
            x2, y2 = project(w/2, y_base, z)
            goto(x1, y1); pendown(); goto(x2, y2)
            
            # Top white cream
            if depth == 0:
                color("white")
                cx, cy = project(0, y_base + h, z)
                penup(); goto(cx - w/2*0.9, cy); pendown()
                goto(cx + w/2*0.9, cy)

    # 10 Beautiful Candles with Flickering Flames
    for i in range(10):
        a = angle * 2.5 + i * 0.75
        cx = math.cos(a) * 50
        cz = math.sin(a) * 50
        px, py = project(cx, -20, 140 + cz*40)
        
        penup(); goto(px, py - 55); pendown()
        pensize(12)
        color(255, 240, 180)
        goto(px, py)
        
        # Realistic flickering flame
        flicker = 10 + math.sin(time.time() * 15 + i) * 7
        color("yellow"); dot(flicker + 8)
        color("orange"); dot(flicker + 4)
        color("red"); dot(flicker)

# Floating 3D "AVIK" with Random Sparkle
def draw_avik(t):
    name = "AVIK"
    for idx, char in enumerate(name):
        x = (idx - 1.5) * 100
        z = 90 + math.sin(t + idx*1.3) * 70
        y = math.sin(t * 1.5 + idx) * 50
        
        px, py = project(x, y, z)
        
        # Random sparkles around letters
        if random.random() < 0.3:
            for _ in range(3):
                sx = px + random.randint(-30,30)
                sy = py + random.randint(-30,30)
                color(random.choice(["#ff00ff","#00ffff","#ffff00"]))
                penup(); goto(sx,sy); pendown(); dot(4)
        
        # Glow layers
        for g in range(12, 0, -3):
            color(*glow(t*0.12, idx + g))
            penup(); goto(px - g//2, py - g//2)
            pendown(); write(char, align="center", font=("Impact", 110, "bold"))
        
        color("white")
        penup(); goto(px, py); pendown()
        write(char, align="center", font=("Impact", 110, "bold"))

# Advanced 3D Particle System + Random Bursts
def particles(t):
    # Continuous flow
    for i in range(110):
        age = (t * 1.2 + i * 8) % 400
        if age < 250:
            radius = age * 2
            x = math.cos(i * 0.3 + t * 0.03) * radius
            y = math.sin(i * 1.4 + t * 0.02) * radius - 120 + age * 0.5
            z = math.sin(i * 0.7) * radius * 0.6 + 80
            
            px, py = project(x, y, z)
            hue = (i + t * 0.5) % 1
            col = colorsys.hsv_to_rgb(hue, 1, 1)
            color(int(col[0]*255), int(col[1]*255), int(col[2]*255))
            penup(); goto(px, py); pendown()
            dot(5 + age // 40)
    
    # Random big bursts every few seconds
    if int(t) % 80 < 3:
        cx, cy = project(random.randint(-200,200), -100, 200)
        for _ in range(50):
            ang = random.uniform(0, 6.28)
            speed = random.uniform(5, 25)
            px = cx + math.cos(ang) * speed * 10
            py = cy + math.sin(ang) * speed * 10
            color(random.choice(["#b8034b","#035040","#f7f715","#3c033c"]))
            penup(); goto(px, py); pendown(); dot(random.randint(8,20))

# Holographic Shifting Title
def title_holo(t):
    txt = "HAPPY BIRTHDAY"
    for offset in range(-5, 6):
        hue = (t * 0.08 + offset * 0.25) % 1
        r,g,b = colorsys.hsv_to_rgb(hue, 1, 1)
        color(int(r*200), int(g*200), int(b*255))
        penup()
        goto(offset * 4, 210 - abs(offset) * 8)
        pendown()
        write(txt, align="center", font=("Arial Black", 52, "bold"))

# MAIN LOOP — FLAWLESS & GORGEOUS
t = 0
while t < 700:
    clear()
    
    # Cosmic gradient background
    for i in range(7):
        hue = (t * 0.008 + i * 0.18) % 1
        col = colorsys.hsv_to_rgb(hue, 0.7, 0.25)
        color(int(col[0]*90), int(col[1]*90), int(col[2]*140))
        penup(); goto(0, -400 + i*100); pendown()
        pensize(380 + i*90)
        circle(480 + math.sin(t*0.04)*80)

    particles(t)
    draw_cake(t * 0.07)
    draw_avik(t * 0.12)
    title_holo(t)

    # Final message with style
    color("#ffffff")
    penup(); goto(0, -230); pendown()
    write("May 2025 bring you magic & success!", align="center", font=("Georgia", 28, "italic bold"))
    goto(0, -270)
    write("Made with pure love & Python", align="center", font=("Courier New", 22, "bold"))

    update()
    t += 1
    time.sleep(0.033)  # ~30 FPS

# FINAL BREATHTAKING FRAME
clear()
bgcolor("#000033")
particles(200)
draw_cake(0)
draw_avik(300)
title_holo(0)

color("#045c5c")
goto(0, 240)
write("HAPPY BIRTHDAY", align="center", font=("Futura", 80, "bold"))

color("#ffff00")
goto(0, -230)
write("AVIK", align="center", font=("Impact", 180, "bold"))

color("#d5086f")
goto(0, -320)
write("Keep Shining Forever!", align="center", font=("Helvetica", 36, "bold italic"))

update()
done()