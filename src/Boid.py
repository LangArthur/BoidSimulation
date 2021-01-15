#
# Created on Fri Aug 14 2020
#
# Copyright (c) BoidSimulation 2020 Arthur Lang
# Boid.py
#

import random
import math

class Boid():
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.width = 20
        self.height = 40
        self._speed = 1

        # random direction at initialisation
        vect = (random.randrange(-100, 100) / 100, random.randrange(-100, 100) / 100)
        # normalize the vector
        norm = math.sqrt(vect[0] * vect[0] + vect[1] * vect[1])
        self._direction = [round(vect[0] / norm, 2), round(vect[1] / norm, 2)]

        self._viewDist = 100
        self._viewAngle = 50

    def __str__(self):
        return "(" + str(self._x) + "," + str(self._y) + ")" + "\nspeed: " + str(self._speed) + "direction(" + str(self._direction[0]) + "," + str(self._direction[1]) + ")"

    def x(self):
        return self._x

    def y(self):
        return self._y

    def direction(self):
        return self._direction

    def view(self):
        return self._viewDist

    def viewRange(self):
        return self._viewAngle

    def update(self, screenWidth, screenHeight):
        # when the boid is out
        if (self.isOut(screenWidth, screenHeight)):
            if (self._x > screenWidth + self.width):
                self._x = 0 - self.height
            elif (self._x < 0 - self.width):
                self._x = screenWidth + self.height
            if (self._y > screenHeight + self.width):
                self._y = 0 - self.height
            elif (self._y < 0 - self.width):
                self._y = screenHeight + self.height
        else:
            self.move()

    def move(self):
        self._x += self._speed * self._direction[0]
        self._y += self._speed * self._direction[1]

    def isOut(self, width, height):
        return self._x - self.height > width or self._x + self.height < 0 or self._y - self.height > height or self._y + self.height < 0

    def rotate(self, angle):
        distX = round(self._direction[0] * math.cos(angle) - self._direction[1] * math.sin(angle), 2)
        if (distX > 1.0):
            distX = 1.0
        elif (distX < -1.0):
            distY = -1.0

        distY = round(self._direction[1] * math.cos(angle) + self._direction[0] * math.sin(angle), 2)
        if (distY > 1):
            distY = 1.0
        elif (distY < -1):
            distY = -1.0
        self._direction[0] = distX
        self._direction[1] = distY


