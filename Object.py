import numpy as np


class Object(object):

    def __init__(self, color=(255, 0, 0), diffuse = (1, 1, 1),
                       specular = (1, 1, 1), phong = 4):
        self.color = color
        self.diffuse = diffuse
        self.specular = specular
        self.phong = phong






class Sphere(Object):

    def __init__(self, color=(255, 0, 0), diffuse = (1, 1, 1),
                 specular = (1, 1, 1), phong = 4,
                 center=(0, 0.1, -3), radius=.5):
        super().__init__(color, diffuse, specular, phong)
        self.center = np.array([center[0], center[1], center[2], 1])
        self.radius = radius


    # If ray intersects, returns the intersection distance. Else returns None.
    def rayIntersectionDistance(self, ray):

        rayOriginIsInsideSphere = False
        if np.linalg.norm(self.center - ray.origin) < self.radius:
            rayOriginIsInsideSphere = True

        OC = self.center - ray.origin
        tca = np.dot(ray.direction, OC)

        if (tca < 0) and (rayOriginIsInsideSphere == False): return None

        thc = self.radius - np.linalg.norm(OC) + tca

        print("rd: " + str(ray.direction) + "       tca: " + str(tca) + "       OC: " + str(OC) + "       thc: " + str(thc) + "      r0 in Sphere: " + str(rayOriginIsInsideSphere))

        if (thc < 0): return None

        intersectionDist = 0
        if rayOriginIsInsideSphere: intersectionDist = tca + thc
        else: intersectionDist = tca - thc

        return intersectionDist






class Triangle(Object):

    def __init__(self, color=(255, 0, 0), diffuse = (1, 1, 1),
                 specular = (1, 1, 1), phong = 4,
                 vertex1=(.3, -.3, -.4),
                 vertex2=(0, .3, -.1),
                 vertex3=(-.3, -.3, .2) ):
        super().__init__(color, diffuse, specular, phong)
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
