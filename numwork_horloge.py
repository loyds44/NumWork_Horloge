import turtle
from time import sleep

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

    turtle.goto(0,-150)

def get_angle(index):
    global secondes, minutes, heures
    if index == 0:
        return 90 - secondes * 6
    elif index == 1:
        return 90 - (minutes * 6 + secondes * 0.1)
    else:
        return 90 - ((heures % 12) * 30 + minutes * 0.5)

def clear(seconde, minute, heure, length):
    index = 0
    turtle.pensize(5)
    for _ in [seconde, minute, heure]:
        turtle.goto(0, 0)
        turtle.setheading(get_angle(index))
        turtle.pendown()
        turtle.pencolor("white")
        turtle.forward(length+3)
        turtle.penup()
        index += 1

def draw(seconde, minute, heure, length):
    index = 0
    turtle.pensize(1)
    for _ in [seconde, minute, heure]:
        turtle.goto(0, 0)
        turtle.setheading(get_angle(index))
        turtle.pendown()
        if index < 1:
            turtle.pencolor("red")
            turtle.forward(length)
        elif index ==1 :
            turtle.pencolor("blue")
            turtle.forward(length+3)
        else :
            turtle.pencolor("black")
            turtle.forward(length+3)
        turtle.penup()
        index += 1

def verification(secondes, minutes, heures):
    secondes += 1
    if secondes > 59:
        secondes = 0
        minutes += 1
        if minutes > 59:
            minutes = 0
            heures += 1
            if heures > 23:
                heures = 0
    return secondes, minutes, heures

old_angle = 90

cadran()
turtle.goto(0, 0)
turtle.setheading(old_angle)
turtle.pendown()
turtle.pencolor("red")
turtle.forward(needle_length)
turtle.penup()


while True:
    sleep(1)
    clear(old_secondes, old_minutes, old_heures, needle_length)
    secondes, minutes, heures = verification(secondes, minutes, heures)
    draw(secondes, minutes, heures, needle_length)
    old_secondes, old_minutes, old_heures = secondes, minutes, heures
