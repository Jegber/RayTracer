import numpy as np
import Ray


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

        o = [0, 0, 0, 0]
        #o = ray.origin
        d = np.subtract(ray.direction, ray.origin)
        c = np.subtract(self.center, ray.origin)
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

        #print("t_0*d: ", t_0*d)
        intersectionPoint = o + d*t_0
        intersectionPoint[3] = 0
        intersectionDist = np.linalg.norm(d*t_0)

        return (intersectionDist, intersectionPoint)




class Triangle(Object):

    def __init__(self, diffuse = (0, 0, 1),
                 specular = (1, 1, 1), phong = 32,
                 vertex1=(.3, -.3, -1.4),
                 vertex2=(0, .3, -1.1),
                 vertex3=(-.3, -.3, -.8) ):
        super().__init__(diffuse, specular, phong)
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        pn = np.cross(np.subtract(self.vertex3, self.vertex2), np.subtract(self.vertex1, self.vertex2))
        pn = Ray.normalized(pn)
        self.plane_normal = pn


    # If ray intersects, returns the intersection distance and intersect point. Else returns None.
    def rayIntersection(self, ray):
        intersectionDist = None
        intersectionPoint = None

        #pn = np.cross(np.subtract(self.vertex3, self.vertex2), np.subtract(self.vertex1, self.vertex2))
        #pn = Ray.normalized(pn)
        vd = np.dot(self.plane_normal, ray.direction[0:3:1])

        if vd == 0: return (intersectionDist, intersectionPoint)

        d = np.dot(self.plane_normal, self.vertex1)
        vo = (np.dot(self.plane_normal, ray.origin[0:3:1]) + d)
        t = vo / vd
        #print("t: ", t)

        if t < 0: return (intersectionDist, intersectionPoint)
        if vd > 0: self.plane_normal = -1 * self.plane_normal

        r = ray.origin + ray.direction*t

        edge1 = np.subtract(self.vertex2, self.vertex1)
        edge2 = np.subtract(self.vertex3, self.vertex2)
        edge3 = np.subtract(self.vertex1, self.vertex3)
        C1 = r[0:3:1] - self.vertex1
        C2 = r[0:3:1] - self.vertex2
        C3 = r[0:3:1] - self.vertex3

        if (  np.dot(self.plane_normal, np.cross(edge1, C1)) > 0 and
              np.dot(self.plane_normal, np.cross(edge2, C2)) > 0 and
              np.dot(self.plane_normal, np.cross(edge3, C3)) > 0      ): return (t, r)


        return (None, None)
