#
# Created on Fri Aug 14 2020
#
# Copyright (c) BoidSimulation 2020 Arthur Lang
# Boid.py
#

import random

class Boid():
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._speed = 1
        self._direction = (random.random(), random.random())

    def __str__(self):
        return "(" + str(self._x) + "," + str(self._y) + ")" + "\nspeed: " + str(self._speed) + "direction(" + str(self._direction[0]) + "," + str(self._direction[1]) + ")"

    def x(self):
        return self._x

    def y(self):
        return self._y

    def compute(self):
        self._x += self._speed * self._direction[0]
        self._y += self._speed * self._direction[1]

