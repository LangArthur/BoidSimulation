#
# Created on Fri Aug 14 2020
#
# Copyright (c) BoidSimulation 2020 Arthur Lang
# Boid.py
#

import random

class Boid():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.direction = (random.random(), random.random())

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")" + "\nspeed: " + str(self.speed) + "direction(" + str(self.direction[0]) + "," + str(self.direction[1]) + ")"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def compute(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

