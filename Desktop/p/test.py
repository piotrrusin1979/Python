from math import cos, sin, radians
from random import randint
import turtle

'''
Module providing physics functions for the game
'''


class pilka(turtle.Turtle):
    def __init__(self, startX=0, startY=0, visibility=False, resolution=100, **kwargs):
        self._color = "blue"
        turtle.Turtle.__init__(self)
        self.setx(startX)
        self.sety(startY)
        self.resolution = resolution
        self.xSpeed = 0
        self.ySpeed = 0
        if visibility:
            self.showturtle()
        else:
            self.hideturtle()
    def __str__(self):
        return ("X: {0:.2f} Y: {1:.2f} xSpeed: {2:.2f} ySpeed {3:.2f}".format(self.xcor(), self.ycor(), self.xSpeed, self.ySpeed))
    
    def kopnijPilke(self, speed, angle):
        gconst = 10
        sign = lambda a: (a>=0) - (a<0)
        self.xSpeed = speed*cos(radians(angle))*sign(self.xSpeed)
        self.ySpeed = speed*sin(radians(angle))
        totalTime = 2*self.ySpeed/gconst
        for i in range(1,self.resolution):
            if self.hitWall(200):
                self.xSpeed = -self.xSpeed
                print("speed change {0}".format(self.xcor()))
            deltaTime1 = (i-1)*totalTime/(self.resolution - 1.0)
            deltaTime2 = i*totalTime/(self.resolution - 1.0)
            self.setx(self.xcor() + ((self.xSpeed * deltaTime2) - (self.xSpeed * deltaTime1)))
            self.sety(self.ycor() + ((self.ySpeed*deltaTime2 - (gconst*deltaTime2*deltaTime2)/2) - (self.ySpeed*deltaTime1 - (gconst*deltaTime1*deltaTime1)/2)))
            print(self)
    def getColor(self):
        return self._color
    
    def setColor(self, newColor):
        if newColor in ("blue", "red"):
            self._color = newColor
    
    color = property(getColor, setColor)
            

    def hitWall(self, wall):
        if abs(self.xcor()) >= wall:
            return True
        else:
            return False


p = pilka(resolution=200)
p.color = "blue"

#for i in range(20):
#    p.kopnijPilke(70- i, 75)
turtle.done()
