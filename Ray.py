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

    def getColor(self, scene):
        # Test collisions on each object.
        closestObject = None
        closestIntersectionDist = None
        for renderable in scene.objects:
            intersectionDist = renderable.rayIntersectionDistance(self)
            print(intersectionDist)
            if intersectionDist is None: continue
            if intersectionDist > 0: # intersections behind the camera are bad
                if (closestIntersectionDist is None) or (intersectionDist < closestIntersectionDist):
                    closestIntersectionDist = intersectionDist
                    closestObject = renderable


        if closestObject is None:
            return scene.bgColor

        return [0, 0, 255]


            # If no collision, color bg

            # If collided, recurse through the collisions and combine






class ReflectedRay(Ray):
    def __init__(self, origin, direction):
        super().__init__(origin, direction)





class TransmittedRay(Ray):
    def __init__(self, origin, direction):
        super().__init__(origin, direction)





class ShadowRay(Ray):
    def __init__(self, origin, direction):
        super().__init__(origin, direction)
