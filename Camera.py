import numpy as np
import math
import Ray


class Camera:

    def __init__(self, lookAt=np.array([0,0,-1]), lookFrom=np.array([0,0,0]), lookUp=np.array([0,1,0]), fov=90, xRes=50, yRes=50):
        self.__lookAt = np.array([lookAt[0], lookAt[1], lookAt[2], 1])
        self.__lookFrom = np.array([lookFrom[0], lookFrom[1], lookFrom[2], 1])
        self.__lookUp = np.array([lookUp[0], lookUp[1], lookUp[2], 1])
        self.__fov = fov
        self.__xRes = xRes
        self.__yRes = yRes
        self.__image = np.full((self.__yRes, self.__xRes, 3), 150)
        self.__window = None
        self.__eye = np.array([0,0,0,1])
        self.generateWindow() # Generate the window's pixel center points
        self.positionCamera() # Move the camera into position


    @property
    def lookAt(self):
        return self.__lookAt
    @lookAt.setter
    def lookAt(self, lookAt):
        self.__lookAt = lookAt


    @property
    def lookFrom(self):
        return self.__lookFrom
    @lookFrom.setter
    def lookFrom(self, lookFrom):
        self.__lookFrom = lookFrom


    @property
    def lookUp(self):
        return self.__lookUp
    @lookUp.setter
    def lookUp(self, lookUp):
        self.__lookUp = lookUp


    @property
    def fov(self):
        return self.__fov
    @fov.setter
    def fov(self, fov):
        self.__fov = fov


    @property
    def xRes(self):
        return self.__xRes
    @xRes.setter
    def xRes(self, xRes):
        self.__xRes = xRes


    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image):
        self.__image = image


    # Generate the initial window, an array of coords that represent screen pixels.
    def generateWindow(self):

        print("Generating Window")
        self.__window = np.ones((self.__yRes, self.__xRes, 4))

        windowWidth = 2 * math.tan(self.__fov / 2)
        distanceBetweenPoints = windowWidth / (self.__xRes-1)
        leftMostX = 0 - (windowWidth / 2)
        topMostY  = distanceBetweenPoints * ((self.__yRes / 2) - .5)

        # Create window with Eye at 0,0,0
        for row in range(self.__yRes):
            for col in range(self.__xRes):
                self.__window[row][col][2] = -1 # Window is -1 z away from the Eye
                self.__window[row][col][0] = leftMostX + (col * distanceBetweenPoints) # x
                self.__window[row][col][1] = topMostY - (row * distanceBetweenPoints) # y
        return


    # Transform the camera to the correct location
    def positionCamera(self):

        lookAt_view = self.__lookAt - self.__lookFrom # Center the lookFrom point to 0,0,0
        camForward = np.array([0,0,-1])

        def angle_between(p1, p2):
            if (np.array_equal(p1, [0, 0]) or np.array_equal(p2, [0, 0])): return 0
            ang1 = np.arctan2(*p1[::-1])
            ang2 = np.arctan2(*p2[::-1])
            return (ang1 - ang2) % (2 * np.pi)

        yRad = angle_between([camForward[0], camForward[2]], [lookAt_view[0], lookAt_view[2]]) # xz plane
        xRad = angle_between([lookAt_view[1], lookAt_view[2]], [camForward[1], camForward[2]]) # yz plane. LookAt and lookFrom are switched flip the rotation angle.

        xRotation = np.matrix( [ [1, 0, 0,  0],
                                 [0, np.cos(xRad), -np.sin(xRad),  0],
                                 [0, np.sin(xRad), np.cos(xRad),  0],
                                 [0, 0, 0,  1] ] )
        yRotation = np.matrix( [ [np.cos(yRad), 0, np.sin(yRad),  0],
                                 [0, 1, 0,  0],
                                 [-np.sin(yRad), 0, np.cos(yRad),  0],
                                 [0, 0, 0,  1] ] )

        combinedRotation = yRotation * xRotation

        for row in range(self.__yRes):
            for col in range(self.__xRes):
                self.__window[row][col] = combinedRotation.dot(self.__window[row][col]) # rotate
                self.__window[row][col] = np.add(self.__window[row][col], self.__lookFrom) # translate
                self.__window[row][col][3] = 1 # reset w to 1


        self.__eye = self.__lookFrom

        return


    def renderScene(self, scene):
        # Cast Rays
        for row in range(self.__yRes):
            for col in range(self.__xRes):
                self.renderPixel(scene, row, col)

        return self.__image



    def renderPixel(self, scene, row, col):
        primaryRay = Ray.PrimaryRay(self.__eye, self.__window[row][col])
        closestObject = None
        closestIntersectionDist = None

        # Test collisions on each object.
        for renderable in scene.objects:
            intersectionDist = renderable.rayIntersectionDistance(primaryRay)
            print(intersectionDist)
            if intersectionDist is None: continue
            if intersectionDist > 0: # intersections behind the camera are bad
                if (closestIntersectionDist is None) or (intersectionDist < closestIntersectionDist):
                    closestIntersectionDist = intersectionDist
                    closestObject = renderable


        if closestObject is not None:
            self.__image[row][col] = [0, 0, 255]


            # If no collision, color bg

            # If collided, recurse through the collisions and combine





        return
