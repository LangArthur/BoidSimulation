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
        self._speed = 1

        # vect = (random.randrange(-100, 0) / 100, random.randrange(-100, 0) / 100)
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

    def update(self):
        self._x += self._speed * self._direction[0]
        self._y += self._speed * self._direction[1]

