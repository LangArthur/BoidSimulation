#
# Created on Fri Aug 14 2020
#
# Copyright (c) BoidSimulation 2020 Arthur Lang
# Boid.py
#

import random
import math

from src.Vector import *

# https://www.red3d.com/cwr/boids/
# https://betterprogramming.pub/boids-simulating-birds-flock-behavior-in-python-9fff99375118

class Boid():

    def __init__(self, id, x, y, interface):
        self.position = Vector(x, y)
        self.id = id
        self.interface = interface
        self.color = [1, 1, 1]
        self.width = 20
        self.height = 40
        self.viewDist = 100
        self.viewAngle = 50

        self._interface = interface
        self._maxSpeed = 5
        self._maxForce = 0.3


        # random direction at initialisation
        vect = (random.randrange(-100, 100) / 100, random.randrange(-100, 100) / 100)
        # normalize the vector
        norm = math.sqrt(vect[0] * vect[0] + vect[1] * vect[1])

        self.velocity = Vector(round(vect[0] / norm, 2), round(vect[1] / norm, 2))
        self.acceleration = Vector(0, 0)

    def update(self, screenWidth, screenHeight):

        neighbors = self._interface.findNeighbor(self.position, self.id)
        self.align(neighbors)
        self.cohesion(neighbors)
        self.seperation(neighbors)
        # when the boid is out
        if (self.isOut(screenWidth, screenHeight)):
            if (self.position.x > screenWidth + self.width):
                self.position.x = 0 - self.height
            elif (self.position.x < 0 - self.width):
                self.position.x = screenWidth + self.height
            if (self.position.y > screenHeight + self.width):
                self.position.y = 0 - self.height
            elif (self.position.y < 0 - self.width):
                self.position.y = screenHeight + self.height
        else:
            self.move()

    # check if the boid is in or out of the window rectangle
    def isOut(self, width, height):
        return self.position.x - self.height > width or self.position.x + self.height < 0 or self.position.y - self.height > height or self.position.y + self.height < 0

    # update the position of the boid
    def move(self):
        self.position += self.velocity
        self.velocity += self.acceleration
        if (self.velocity.squaredMagnitude() > math.pow(self._maxSpeed, 2)):
            self.velocity.normalize() 
            self.velocity *= self._maxSpeed
        self.acceleration[0] = 0
        self.acceleration[1] = 0

    # rotate the boid
    def rotate(self, angle):
        distX = round(self.velocity[0] * math.cos(angle) - self.velocity[1] * math.sin(angle), 2)
        if (distX > 1.0):
            distX = 1.0
        elif (distX < -1.0):
            distY = -1.0

        distY = round(self.velocity[1] * math.cos(angle) + self.velocity[0] * math.sin(angle), 2)
        if (distY > 1):
            distY = 1.0
        elif (distY < -1):
            distY = -1.0
        self.velocity[0] = distX
        self.velocity[1] = distY


    # return true if the position collide with the boid vision zone
    def collide(self, position):
        return math.pow(self.viewDist, 2) > squareDist(position, self.position)

    # collision with ovaloid hitbox (may be useful in future)
    # def preciseCollide(self, x, y):
    #     return ((math.pow((position.x - self.position.x), 2) // math.pow(self.width / 2, 2)) + (math.pow((position.y - self.position.y), 2) // math.pow(self.height / 2, 2)) <= 1)

    # align rule
    def align(self, neighbors):
        nbrNeighbors = len(neighbors)
        if (nbrNeighbors > 0):
            # get average velocity
            average = Vector(0, 0)
            for neighbor in neighbors:
                average += neighbor.velocity
            average += self.velocity
            average /= (nbrNeighbors + 1)
            average.normalize()
            steering = average - self.velocity
            self.acceleration += steering

    # cohesion rule
    def cohesion(self, neighbors):
        nbrNeighbors = len(neighbors)
        if (nbrNeighbors > 0):
            # get center of mass
            centerOfMass = Vector(0, 0)
            for neighbor in neighbors:
                centerOfMass += neighbor.position
            centerOfMass += self.position
            centerOfMass /= (nbrNeighbors + 1)
            centerOfMass -= self.position
            # control the speed
            if (centerOfMass.squaredMagnitude() > 0):
                centerOfMass.normalize()
                centerOfMass *= self._maxSpeed
            steering = centerOfMass - self.velocity
            if (steering.squaredMagnitude() > math.pow(self._maxForce, 2)):
                steering.normalize()
                steering *= self._maxForce
            self.acceleration += steering

    # separation rule
    def seperation(self, neighbors):
        nbrNeighbors = len(neighbors)
        if (nbrNeighbors > 0):
            average = Vector(0, 0)
            for neighbor in neighbors:
                diff = self.position - neighbor.position
                magnitude = diff.magnitude()
                if (magnitude != 0):
                    diff /= diff.magnitude()
                average += diff
            average /= nbrNeighbors
            if (average.magnitude() > 0):
                average.normalize()
                average *= self._maxSpeed
            steering = average - self.velocity
            if (steering.magnitude() > math.pow(self._maxForce, 2)):
                steering.normalize()
                steering *= self._maxForce
            self.acceleration += steering
