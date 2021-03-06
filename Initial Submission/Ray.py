import numpy as np
import Object

class Ray(object):

    def __init__(self, origin, direction, bouncesLeft = 0, shouldNormalize=True):
        origin[3] = 0
        self.origin = origin
        direction[3] = 0
        self.direction = normalized(a=np.subtract(direction, origin)) + origin if shouldNormalize == True else direction
        self.direction[3] = 0
        self.bouncesLeft = bouncesLeft


    def computePhongColor(self, intersection, scene, object):
        color = [0, 0, 0]

        if type(object) is Object.Triangle:
            N_Normalized = np.append(object.plane_normal, 0)


        if type(object) is Object.Sphere:
            N = intersection[1] - object.center
            N_Normalized = Ray([0, 0, 0, 0], N).direction



        reflectionDirection = 2*N_Normalized * (N_Normalized.dot(scene.directionToLight)) - (scene.directionToLight)
        reflectedRay = ReflectedRay([0,0,0,0], reflectionDirection,
                                        bouncesLeft = self.bouncesLeft - 1)
        r_Normalized = reflectedRay.direction
        e_Normalized = Ray([0,0,0,0], scene.camera.eye - intersection[1]).direction
        shadow = 0 if self.pointIsInShadow(intersection[1], scene) else 1


        for rgb in range(3):
            color[rgb] = object.diffuse[rgb]    *    (scene.ambientLight[rgb] + shadow*scene.directionalLightColor[rgb] * max(0, N_Normalized.dot(scene.directionToLight)))    +     shadow*scene.directionalLightColor[rgb]*object.specular[rgb]*max(0, np.dot(r_Normalized, e_Normalized))**object.phong
            color[rgb] = np.interp(color[rgb], (0, 1), (0, 255))

        return color


    def pointIsInShadow(self, intersectionPoint, scene):
        startingPoint = intersectionPoint
        directionPoint = intersectionPoint + scene.directionToLight
        directionPoint[3] = 0
        offsetStartingPoint = [i for i in startingPoint + directionPoint * .0000001]
        #print()
        #print("offsetStartingPoint: ", offsetStartingPoint)
        #print("offsetStartingPoint: ", offsetStartingPoint)
        #print("directionToLight: ", scene.directionToLight)
        #print("directionPoint: ", directionPoint)

        shadowRay = Ray(offsetStartingPoint, directionPoint,  shouldNormalize = True)
        #print("shadowRay origin: ", shadowRay.origin, "   dest: ", shadowRay.direction)

        closestCollision = shadowRay.getClosestIntersection(scene)
        closestCollisionObject = closestCollision[2]
        collisionDistance = closestCollision[0]

        if collisionDistance is None: return False

        if collisionDistance < .00001:
            farthestObject = shadowRay.getFarthestIntersection(scene)[2]
            if farthestObject is closestCollisionObject: return False
            return True # This is a hack. For some reason rays kept colliding with [0,0,0]

        return True # shadow ray collided with something. You're in shadow.


    def getClosestIntersection(self, scene):
        # Test collisions on each object.
        #print("ray origin: ", self.origin, "     ray direction: ", self.direction)
        closestObject = None
        closestIntersection = (None, None)
        for object in scene.objects:
            intersection = object.rayIntersection(self)
            if intersection[0] is None: continue # If the ray didn't hit anything
            if closestIntersection[0] is None: closestIntersection = intersection
            if intersection[0] <= closestIntersection[0]:
                closestIntersection = intersection
                closestObject = object

        #print("closestIntersectionPoint: ", closestIntersection[1])
        #if closestObject is not None: print("closestIntersectionObject: ", closestObject.center)

        #       distance               intersection point      object
        return (closestIntersection[0], closestIntersection[1], closestObject)

    def getFarthestIntersection(self, scene):
        # Test collisions on each object.
        #print("ray origin: ", self.origin, "     ray direction: ", self.direction)
        farthestObject = None
        farthestIntersection = (None, None)
        for object in scene.objects:
            intersection = object.rayIntersection(self)
            if intersection[0] is None: continue # If the ray didn't hit anything
            if farthestIntersection[0] is None: farthestIntersection = intersection
            if intersection[0] >= farthestIntersection[0]:
                farthestIntersection = intersection
                farthestObject = object

        #print("closestIntersectionPoint: ", closestIntersection[1])
        #if closestObject is not None: print("closestIntersectionObject: ", closestObject.center)

        #       distance               intersection point      object
        return (farthestIntersection[0], farthestIntersection[1], farthestObject)



class PrimaryRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)


    def getColor(self, scene):
        intersection = self.getClosestIntersection(scene)
        closestObject = intersection[2]
        closestIntersection = intersection[0:2:1]

        if closestObject is None: # If no collision, color bg
            return scene.bgColor

        if self.bouncesLeft <= 0: # If no more bounces left, return object color
            return self.computePhongColor(closestIntersection, scene, closestObject)

        if closestObject.isReflective():

            n = intersection[1] - closestObject.center
            n_n = Ray([0, 0, 0, 0], n).direction
            #print("n_n: ", n_n)

            d = self.origin - intersection[1]
            d_n = Ray([0, 0, 0, 0], d).direction
            #print("d_n: ", d_n)

            r = d_n - 2*n_n*(np.dot(d_n, n_n))
            r_n = -Ray([0, 0, 0, 0], r).direction
            #print("r_n: ", r_n)


            startPoint = [i for i in intersection[1] + (intersection[1]-closestObject.center)*.0000001]


            reflectedRay = PrimaryRay(startPoint, r_n + intersection[1], bouncesLeft=self.bouncesLeft-1)



            return np.multiply(reflectedRay.getColor(scene), .75)

            """
            d = Ray(intersection[1], self.origin).direction - closestObject.center
            d_Normalized = Ray([0, 0, 0, 0], d).direction
            d_Normalized[3] = 0
            print("d_Normalized: ", d_Normalized)

            N = intersection[1] - closestObject.center
            N[3] = 0
            #print("N: ", N)
            N_Normalized = Ray([0, 0, 0, 0], N).direction
            print("n_Normalized: ", N_Normalized)

            reflectionDirection = d_Normalized - 2*N_Normalized*(np.dot(d_Normalized, N_Normalized))
            r_Normalized = Ray([0, 0, 0, 0], reflectionDirection).direction
            print("r_Normalized: ", reflectionDirection)


            startingPoint = intersection[1]
            directionPoint = intersection[1] + r_Normalized + closestObject.center
            directionPoint[3] = 0
            offsetStartingPoint = [i for i in startingPoint + directionPoint * .00001]
            print("startingPoint: ", startingPoint)
            print("directionPoint: ", directionPoint)


            reflectedRay = PrimaryRay(offsetStartingPoint, directionPoint, bouncesLeft = self.bouncesLeft - 1)
            print("reflectedRayOrigin: ", reflectedRay.origin)
            print("reflectedRayDirection: ", reflectedRay.direction)


            return np.multiply(reflectedRay.getColor(scene), .75)
            """


        # If collided, recurse through the collisions and combine

        #print(color)
        return self.computePhongColor(closestIntersection, scene, closestObject)


def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return (a / np.expand_dims(l2, axis))[0]









class ReflectedRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)





class TransmittedRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)





class ShadowRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)
