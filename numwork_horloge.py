import turtle
import time

needle_length = 90
secondes = 0
minutes = int(input("Minute :"))
heures = int(input("Heure :"))
initial_total = heures * 3600 + minutes * 60 #permet de savoir le nbr de secondes de depart par rapport a ce qu'a mis l'uitlisateur 
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
    turtle.pencolor("white")
    for _ in range(3):
        turtle.goto(0, 0)
        turtle.setheading(get_angle(index, sec, min, hr))
        turtle.pendown()
        turtle.forward(length + 5)
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
            turtle.forward(length + 5)
        turtle.penup()
        index += 1

cadran()
start = time.monotonic()
while True:
    temps_loop = time.monotonic()
    clear(old_secondes, old_minutes, old_heures, needle_length)
    draw(secondes, minutes, heures, needle_length)
    old_secondes, old_minutes, old_heures = secondes, minutes, heures

    temps_loop = time.monotonic()-temps_loop
    if temps_loop <1:
        time.sleep(1 - temps_loop )

    temps_ecoule = int(time.monotonic() - start) + initial_total
    secondes = temps_ecoule % 60
    minutes = (temps_ecoule // 60) % 60
    heures   = (temps_ecoule // 3600) % 24

    #print(heures, minutes, secondes)
