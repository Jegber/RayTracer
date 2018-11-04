import numpy as np


class Object(object):

    def __init__(self, diffuse = (1, 1, 1), specular = (1, 1, 1), phong = 4):
        self.diffuse = diffuse
        self.specular = specular
        self.phong = phong






class Sphere(Object):

    def __init__(self, diffuse = (1, 0, 0),
                 specular = (1, 1, 1), phong = 4,
                 center=(1, 1, -10), radius=1):
        super().__init__(diffuse, specular, phong)
        self.center = np.array([center[0], center[1], center[2], 1])
        self.radius = radius


    # If ray intersects, returns the intersection distance and intersect point. Else returns None.
    def rayIntersection(self, ray):

        o = ray.origin
        d = ray.direction
        c = self.center
        r = self.radius


        #print("ro: " + str(o) + "   rd: " + str(d) + "                           cc: " + str(c) + "   cr: " + str(r))


        #B = 2 * (d[0]*o[0] - d[0]*c[0] + d[1]*o[1] - d[1]*c[1] + d[2]*o[2] - d[2]*c[2])
        B = 2 * ( d[0]*(o[0] - c[0]) + d[1]*(o[1] - c[1]) + d[2]*(o[2] - c[2]) )
        #C = o[0]**2 - 2*o[0]*c[0] + c[0]**2 + o[1]**2 - 2*o[1]*c[1]+ c[1]**2 + o[2]**2 - 2*o[2]*c[2] + c[2]**2 - r**2
        C = (o[0]-c[0])**2 + (o[1]-c[1])**2 + (o[2]-c[2])**2 - r**2
        D = B**2 - 4*C

        #print("B: " + str(B) + "   C: " + str(C) + "   D: " + str(D))

        if D < 0: return (None, None)

        t_0 = (-B - np.sqrt(D)) / 2

        if t_0 <= 0:
            t_1 = (-B + np.sqrt(D)) / 2
            if t_1 <= 0: return (None, None)
            t_0 = t_1

        intersectionPoint = o + d*t_0
        intersectionPoint[3] = 0
        intersectionDist = np.linalg.norm(intersectionPoint - o)

        return (intersectionDist, intersectionPoint)






class Triangle(Object):

    def __init__(self, diffuse = (1, 1, 1),
                 specular = (1, 1, 1), phong = 4,
                 vertex1=(.3, -.3, -.4),
                 vertex2=(0, .3, -.1),
                 vertex3=(-.3, -.3, .2) ):
        super().__init__(diffuse, specular, phong)
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
