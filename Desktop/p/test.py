from math import cos, sin, radians
from random import randint
import turtle

'''
Module providing physics functions for the game
'''

def rzut(speed, angle, gconst, resolution):
    '''
    speed - w metrach na sekunde
    angle kat rzutu wzgledem podloza
    gConst - przyspieszenie ziemskie
    resolution - ilosc punktow do zwrotu
    '''
    xSpeed = speed*cos(radians(angle))
    ySpeed = speed*sin(radians(angle))
    totalTime = 2*ySpeed/gconst
    for i in range(resolution):
        deltaTime = i*totalTime/(resolution - 1.0)
        deltaX = xSpeed * deltaTime
        deltaY = ySpeed*deltaTime - (gconst*deltaTime*deltaTime)/2
        yield (deltaX, deltaY)

    print("Dla V {2} oraz kąta {3}: xSpeed to {0:.2f}, a ySpeed to {1:.2f}, czas lotu {4}".format(xSpeed, ySpeed, speed, angle, totalTime))


if __name__ == "__main__a":
    for k in rzut(25, 45, 10, 100):
        print("DeltaX = {0:.2f}, Delta Y = {1:.2f}".format(k[0], k[1]))

zolwik = turtle.Turtle()
zolwik.color("blue")
zolwik.setx(0)
zolwik.sety(0)


while True:
    for coords in rzut(randint(0, 40), randint(0, 180), 10, 60):
        zolwik.setx(coords[0])
        zolwik.sety(coords[1])
