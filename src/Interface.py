#!/usr/bin/python3

#
# Created on Mon Aug 10 2020
#
# Copyright (c) BoidSimulation 2020 Arthur Lang
# Interface.py
#

import math
import pyglet
from pyglet.window import key, mouse
from pyglet.gl import *

from src.Boid import *


class Interface():
    def __init__(self):
        self._width = 1280
        self._height = 720
        self.window = pyglet.window.Window(self._width, self._height, caption="BoidSimulation")
        self.boids = []
        # add event handlers
        self.window.push_handlers(self.on_key_press)
        self.window.push_handlers(self.on_mouse_press)
        # next id availble for boids
        self._availableId = 0

        self.debug = False
        pyglet.clock.schedule_interval(self.loop, 1 / 60)

    # keyboard event
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.debug = (self.debug == False)

    # keyboard event
    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            newBoid = Boid(self._availableId, x, y, self)
            self.boids.append(newBoid)
            self._availableId += 1

    def draw(self):
        pyglet.clock.tick()
        #clear the window
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        for boid in self.boids:
            self.drawBoid(boid)
        print("FPS: {}\t there are {} boids".format(round(pyglet.clock.get_fps(), 2), len(self.boids)), end='\r')

    # draw a boid
    def drawBoid(self, boid):

        x = boid.position.x
        y = boid.position.y
        direction = boid.velocity
        direction.normalize()
        color = boid.color
        # set drawing color
        glColor3f(color[0], color[1], color[2])

        # compute the angle
        rotateAngle = math.acos(direction[0])
        # fix angle is direction is negative
        if (direction[1] < 0):
            rotateAngle = 2 * math.pi - rotateAngle 
        # compute distances
        cosDist = math.cos(rotateAngle)
        sinDist = math.sin(rotateAngle)

        # draw the boid
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
            [0, 1, 2, 0, 3, 2],
            ('v2f', (x - (boid.height * (1 / 4) * cosDist), y - (boid.height * (1 / 4) * sinDist),
                    # right wing
                    x + (boid.width / 2 * sinDist) - (boid.height * (1 / 2) * cosDist), y - (boid.width / 2 * cosDist) - (boid.height * (1 / 2) * sinDist),
                    # top
                    x + (boid.height * (1 / 2) * cosDist), y + (boid.height * (1 / 2) * sinDist),
                    # left wing
                    x - (boid.width / 2 * sinDist) - (boid.height * (1 / 2) * cosDist), y + (boid.width / 2 * cosDist) - (boid.height * (1 / 2) * sinDist),
            ))
        )

        if (self.debug):
            self.printBoidView(boid)

    # display use when debug mode is active
    def printBoidView(self, boid):
        glColor3f(1,0,0)

        direction = boid.velocity
        direction.normalize()
        x = boid.position.x
        y = boid.position.y

        pyglet.graphics.draw_indexed(2, pyglet.gl.GL_LINES,
            [0, 1],
            ('v2f', (x, y,
                x + direction[0] * boid.viewDist, y + direction[1] * boid.viewDist               
            ))
        )

    # main loop of the programm
    def loop(self, dt):
        self.update()
        self.draw()

    def update(self):
        # update all boids
        for boid in self.boids:
            boid.update(self._width, self._height)

    def run(self):
        pyglet.app.run()

    # return all the neighbors of a specific boid
    def findNeighbor(self, position, id):
        res = []
        for boid in self.boids:
            if (boid.id != id and boid.collide(position)):
                res.append(boid)
        return res
