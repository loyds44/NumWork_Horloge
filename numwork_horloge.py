import turtle
import time

needle_length = 90
secondes = 0
minutes = int(input("Minute :"))
heures = int(input("Heure :"))
initial_total = heures * 3600 + minutes * 60  # convertir en secondes de depart

old_secondes, old_minutes, old_heures = secondes, minutes, heures
old_angles = [0, 0, 0]  # pour enregistrer les anciens angles de l'aiguille
start = time.monotonic() #permet de lancer le compte des secondes 


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
        return 90 - (min + (sec // 30) * 0.5) * 6
    else:
        return 90 - (((hr % 12) + min / 60) * 30)


def clear(length, old_angles, new_angles):
    turtle.pensize(5)
    turtle.pencolor("white")
    for index in range(3):
        if old_angles[index] != new_angles[index]:  #efface seulement si l'ange change 
            turtle.goto(0, 0)
            turtle.setheading(old_angles[index])  #permet d'utiliser l'ancien angle
            turtle.pendown()
            turtle.forward(length + (5 if index == 2 else (3 if index == 1 else 0))) #adapte la taille de l'aiguille
            turtle.penup()

def draw(sec, min, hr, length):
    index = 0
    turtle.pensize(1)
    for _ in range(3):
        turtle.goto(0, 0)
        angle = get_angle(index, sec, min, hr)
        turtle.setheading(angle)
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

while True:
    temps_loop = time.monotonic()
    
    new_angles = [get_angle(i, secondes, minutes, heures) for i in range(3)]
    clear(needle_length, old_angles, new_angles)
    draw(secondes, minutes, heures, needle_length)
    old_angles = new_angles.copy()

    temps_loop = time.monotonic() - temps_loop
    if temps_loop < 1:
        time.sleep(1 - temps_loop)

    temps_ecoule = int(time.monotonic() - start) + initial_total
    secondes = temps_ecoule % 60
    minutes = (temps_ecoule // 60) % 60
    heures = (temps_ecoule // 3600) % 24

    print(heures, minutes, secondes)
