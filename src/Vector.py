#
# Created on Thu Jun 17 2021
#
# Arthur Lang
# Vector.py
#

import math

class Vector():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("(" + str(self.x) + "," + str(self.y) + ")")

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, value):
        if (type(value) is int or type(value) is float):
            return Vector(self.x * value, self.y * value)
        else:
            raise ValueError("Immposible to multiply with " + type(value) + "type.")

    def __truediv__(self, value):
        if ((type(value) is float or type(value) is int) and value != 0):
            return Vector(self.x / value, self.y / value)
        else:
            raise ValueError("Impossible to divide with this value " + str(value))

    def __getitem__(self, key):
        if (key == 0):
            return self.x
        elif (key == 1):
            return self.y
        else:
            raise ValueError("Error: bad index for a vector")

    def __setitem__(self, key, value):
        if (key == 0):
            self.x = value
        elif (key == 1):
            self.y = value
        else:
            raise ValueError("Error: bad index for a vector")

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def squaredMagnitude(self):
        return self.x * self.x + self.y * self.y

    def normalize(self):
        magnitude = self.magnitude()
        self.x /= magnitude
        self.y /= magnitude

def squareDist(vec1, vec2):
    return (math.pow(vec1[0] - vec2[0], 2) + math.pow(vec1[1] - vec2[1], 2) )