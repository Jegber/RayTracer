import numpy as np

class Ray(object):

    def __init__(self, origin, direction, bouncesLeft = 0):
        self.origin = origin
        direction[3] = 0
        self.direction = self.normalized(direction)
        self.direction[3] = 0
        self.bouncesLeft = bouncesLeft


    def normalized(self, a, axis=-1, order=2):
        l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
        l2[l2==0] = 1
        return (a / np.expand_dims(l2, axis))[0]

    def computePhongColor(self, intersection, scene, object):
        N = intersection[1] - object.center
        N_Normalized = Ray([0, 0, 0, 0], N).direction
        reflectionDirection = 2*N_Normalized * (N_Normalized.dot(scene.directionToLight)) - (scene.directionToLight)
        reflectedRay = ReflectedRay([0,0,0,0], reflectionDirection,
                                    bouncesLeft = self.bouncesLeft - 1)
        r_Normalized = reflectedRay.direction
        e_Normalized = Ray([0,0,0,0], scene.camera.eye - intersection[1]).direction
        shadow = 0 #if self.pointIsInShadow(intersection, scene) else 1

        color = [0, 0, 0]
        for rgb in range(3):
            color[rgb] = object.diffuse[rgb]    *    (scene.ambientLight[rgb] + scene.directionalLightColor[rgb] * max(0, N_Normalized.dot(scene.directionToLight)))    +     scene.directionalLightColor[rgb]*object.specular[rgb]*max(0, np.dot(r_Normalized, e_Normalized))**object.phong
            color[rgb] = np.interp(color[rgb], (0, 1), (0, 255))

        return color


    def pointIsInShadow(self, intersection, scene):
        ray = PrimaryRay(intersection[1], intersection[1] + scene.directionToLight, 0)

        return ray.getColor(scene)


    def getClosestIntersection(self, scene):
        pass




class PrimaryRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)


    def getColor(self, scene):
        # Test collisions on each object.
        closestObject = None
        closestIntersection = (None, None)
        for object in scene.objects:
            intersection = object.rayIntersection(self)
            if intersection[0] is None: continue # If the ray didn't hit anything
            if closestIntersection[0] is None: closestIntersection = intersection
            if intersection[0] <= closestIntersection[0]:
                closestIntersection = intersection
                closestObject = object

        if closestObject is None: # If no collision, color bg
            return scene.bgColor

        if self.bouncesLeft <= 0: # If no more bounces left, return object color
            return self.computePhongColor(closestIntersection, scene, closestObject)


        #R1 = -(self.origin - closestIntersection[1])
        R1 = -(self.origin - closestIntersection[1])
        R1[3] = 0
        R1_Normalized = Ray([0,0,0,0], R1).direction
        R1_Normalized[3] = 0
        N = closestIntersection[1] - closestObject.center
        N_Normalized = Ray([0, 0, 0, 0], N).direction
        N_Normalized[3] = 0
        reflectionDirection = R1_Normalized - 2*N_Normalized * (R1_Normalized.dot(N_Normalized))
        reflectionDirection[3] = 0
        reflectedRay = ReflectedRay(closestIntersection[1], reflectionDirection + closestIntersection[1],
                                    bouncesLeft = self.bouncesLeft - 1)
        """
        print("\noo: " + str(self.origin) + "     oi:" + str(closestIntersection[1]) + \
              "\nro: " + str(reflectedRay.origin) + "    rd: " + str(reflectedRay.direction))
        """

        if self.direction[0] == 0 and self.direction[1] == 0:
            print("R1: ", R1)
            print("R1_Normalized: ", R1_Normalized)
            print("Closest intersection: ", closestIntersection[1])
            print("N: ", N)
            print("N_Normalized: ", N_Normalized)
            print("ReflectionDirection: ", reflectionDirection)
            print("reflectedRayOrigin: ", reflectedRay.origin)
            print("reflectedRayDirection: ", reflectedRay.direction)
            print()

        color = [0, 0, 0]
        for rgb in range(3):
            color[rgb] = closestObject.diffuse[rgb] * \
                         ( scene.ambientLight[rgb] + \
                           scene.directionalLightColor[rgb] * \
                           max(0, N_Normalized.dot(scene.directionToLight))  ) +\
                         scene.directionalLightColor[rgb] * closestObject.specular[rgb] *\
                         max(0, (reflectedRay.direction-closestIntersection[1]).dot(scene.camera.eye - closestIntersection[1]))**closestObject.phong

        #print(color)
        return color






        # If collided, recurse through the collisions and combine






class ReflectedRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)





class TransmittedRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)





class ShadowRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)
