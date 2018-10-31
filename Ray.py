import numpy as np

class Ray(object):

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
"""
    @property
    def origin(self):
        return self.origin
    @origin.setter
    def origin(self, origin):
        self.origin = origin


    @property
    def direction(self):
        return self.direction
    @direction.setter
    def direction(self, direction):
        self.direction = direction
"""

class PrimaryRay(Ray):
    def __init__(self, origin, direction):
        super().__init__(origin, direction)





class ReflectedRay(Ray):
    def __init__(self, origin, direction):
        super().__init__(origin, direction)





class TransmittedRay(Ray):
    def __init__(self, origin, direction):
        super().__init__(origin, direction)





class ShadowRay(Ray):
    def __init__(self, origin, direction):
        super().__init__(origin, direction)
