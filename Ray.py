import numpy as np

class Ray(object):

    def __init__(self, origin, direction, bouncesLeft = 0, shouldNormalize=True):
        origin[3] = 0
        self.origin = origin
        direction[3] = 0
        self.direction = self.normalized(np.subtract(direction, origin)) + origin if shouldNormalize == True else direction
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
        shadow = 0 if self.pointIsInShadow(intersection[1], scene) else 1
        #shadow = 1

        color = [0, 0, 0]
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



        # If collided, recurse through the collisions and combine

        #print(color)
        return color













class ReflectedRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)





class TransmittedRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)





class ShadowRay(Ray):
    def __init__(self, origin, direction, bouncesLeft):
        super().__init__(origin, direction, bouncesLeft)
