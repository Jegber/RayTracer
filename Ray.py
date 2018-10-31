import numpy as np

class Ray(ray):

    def __init__(self, origin, direction):
        self._origin = origin
        self._directon = direction

    @property
    def origin(self):
        return self._origin
    @origin.setter
    def origin(self, origin):
        self._origin = origin


    @property
    def direction(self):
        return self._direction
    @direction.setter
    def direction(self, direction):
        self._direction = direction


class PrimaryRay(Ray):
    def __init__(self, origin, direction):
        Ray.__init__(self, origin, direction)





class ReflectedRay(Ray):
    def __init__(self, origin, direction):
        Ray.__init__(self, origin, direction)





class TransmittedRay(Ray):
    def __init__(self, origin, direction):
        Ray.__init__(self, origin, direction)





class ShadowRay(Ray):
    def __init__(self, origin, direction):
        Ray.__init__(self, origin, direction)
