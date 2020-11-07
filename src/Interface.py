#!/usr/bin/python3

#
# Created on Mon Aug 10 2020
#
# Copyright (c) BoidSimulation 2020 Arthur Lang
# Interface.py
#

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

        # set clock
        pyglet.clock.schedule_interval(self.loop, 1 / 60)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            print('The space key was pressed.')

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
        # set drawing color
        glColor3f(1,1,1)

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
            [0, 1, 2, 0, 3, 2],
            ('v2f', (x, y,
                    x - 30, y - 10,
                    x, y + 30,
                    x + 30, y - 10,
            ))
        )

    def loop(self, dt):
        self.draw()

    def run(self):
        pyglet.app.run()