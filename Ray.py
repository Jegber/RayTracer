import numpy as np

class Ray(object):

    def __init__(self, origin, direction):
        self.origin = origin
        direction[3] = 0
        self.direction = self.normalized(direction)
        direction[3] = 1


    def normalized(self, a, axis=-1, order=2):
        l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
        l2[l2==0] = 1
        return (a / np.expand_dims(l2, axis))[0]
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
            #print(intersectionDist); print()
            if intersectionDist is None: continue # If the ray didn't hit anything
            if closestIntersectionDist is None: closestIntersectionDist = intersectionDist
            if intersectionDist <= closestIntersectionDist:
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
