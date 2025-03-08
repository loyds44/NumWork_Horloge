import turtle
import time

needle_length = 90
secondes = 0
minutes = int(input("Minute :"))
heures = int(input("Heure :"))
old_secondes, old_minutes, old_heures = secondes, minutes, heures

turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)

def cadran():
    rayon = 100
    taille_barre = 6
    angle_step = 45
    turtle.penup()
    turtle.goto(0, -rayon)
    turtle.pendown()
    turtle.circle(rayon)
    turtle.penup()
    for angle in range(0, 360, angle_step):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(angle)
        turtle.forward(rayon)
        turtle.pendown()
        turtle.backward(taille_barre)
        turtle.penup()

def get_angle(index, sec, min, hr):
    if index == 0:
        return 90 - sec * 6
    elif index == 1:
        return 90 - (min * 6 + sec * 0.1)
    else:
        return 90 - ((hr % 12) * 30 + min * 0.5)

def clear(sec, min, hr, length):
    index = 0
    turtle.pensize(5)
    for _ in range(3):
        turtle.goto(0, 0)
        turtle.setheading(get_angle(index, sec, min, hr))
        turtle.pendown()
        turtle.pencolor("white")
        turtle.forward(length + 3)
        turtle.penup()
        index += 1

def draw(sec, min, hr, length):
    index = 0
    turtle.pensize(1)
    for _ in range(3):
        turtle.goto(0, 0)
        turtle.setheading(get_angle(index, sec, min, hr))
        turtle.pendown()
        if index == 0:
            turtle.pencolor("red")
            turtle.forward(length)
        elif index == 1:
            turtle.pencolor("blue")
            turtle.forward(length + 3)
        else:
            turtle.pencolor("black")
            turtle.forward(length + 3)
        turtle.penup()
        index += 1

def verification(sec, min, hr):
    if sec > 59:
        sec = 0
        min += 1
        if min > 59:
            min = 0
            hr += 1
            if hr > 23:
                hr = 0
    return sec, min, hr

old_angle = 90

cadran()
turtle.goto(0, 0)
turtle.setheading(old_angle)
turtle.pendown()
turtle.pencolor("red")
turtle.forward(needle_length)
turtle.penup()

start = time.monotonic()
while True:
    clear(old_secondes, old_minutes, old_heures, needle_length)
    draw(secondes, minutes, heures, needle_length)
    old_secondes, old_minutes, old_heures = secondes, minutes, heures

    temps_ecoule = time.monotonic() - start
    secondes = int(temps_ecoule) % 60
    minutes = int(minutes + (secondes + temps_ecoule) // 60) % 60
    heures = int(heures + (minutes + temps_ecoule // 60) // 60) % 24

    print(heures, minutes, secondes)
