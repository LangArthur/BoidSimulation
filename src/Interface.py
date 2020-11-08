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
        self.window = pyglet.window.Window(1280, 720, caption="BoidSimulation")
        self.boids = []
        # add event handlers
        self.window.push_handlers(self.on_key_press)
        self.window.push_handlers(self.on_mouse_press)

        self.debug = False

        # set clock
        pyglet.clock.schedule_interval(self.loop, 1 / 60)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.debug = (self.debug == False)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            newBoid = Boid(x, y)
            self.boids.append(newBoid)

    def draw(self):
        #clear the window
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

        for boid in self.boids:
            self.drawBoid(boid)

    def drawBoid(self, boid):

        x = boid.x()
        y = boid.y()
        direction = boid.direction()
        # set drawing color
        glColor3f(1,1,1)

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
            ('v2f', (x, y,
                    x + (10 * sinDist) - (10 * cosDist), y - (10 * cosDist) - (10 * sinDist),
                    x + (30 * cosDist), y + (30 * sinDist),
                    x - (10 * sinDist) - (10 * cosDist), y + (10 * cosDist) - (10 * sinDist),
            ))
        )

        if (self.debug):
            self.printBoidView(boid)

    def printBoidView(self, boid):
        glColor3f(1,0,0)

        direction = boid.direction()
        x = boid.x()
        y = boid.y()

        pyglet.graphics.draw_indexed(2, pyglet.gl.GL_LINES,
            [0, 1],
            ('v2f', (x, y,
                x + direction[0] * boid.view(), y + direction[1] * boid.view()                
            ))
        )

    def loop(self, dt):
        for boid in self.boids:
            boid.update()
        self.draw()

    def run(self):
        pyglet.app.run()