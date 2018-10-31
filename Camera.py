import numpy as np
import math


class Camera:

    def __init__(self, lookAt=np.array([0,0,0]), lookFrom=np.array([0,0,1]), lookUp=np.array([0,1,0]), fov=28, xRes=4, yRes=3):
        self._lookAt = np.array([lookAt[0], lookAt[1], lookAt[2], 1])
        self._lookFrom = np.array([lookFrom[0], lookFrom[1], lookFrom[2], 1])
        self._lookUp = np.array([lookUp[0], lookUp[1], lookUp[2], 1])
        self._fov = fov
        self._xRes = xRes
        self._yRes = yRes
        self._image = np.full((self._yRes, self._xRes, 3), 150)
        self._window = None
        self._eye = np.array([0,0,0,1])
        self.generateWindow()
        self.positionCamera() # Move the camera into position


    @property
    def lookAt(self):
        return self._lookAt
    @lookAt.setter
    def lookAt(self, lookAt):
        self._lookAt = lookAt


    @property
    def lookFrom(self):
        return self._lookFrom
    @lookFrom.setter
    def lookFrom(self, lookFrom):
        self._lookFrom = lookFrom


    @property
    def lookUp(self):
        return self._lookUp
    @lookUp.setter
    def lookUp(self, lookUp):
        self._lookUp = lookUp


    @property
    def fov(self):
        return self._fov
    @fov.setter
    def fov(self, fov):
        self._fov = fov


    @property
    def xRes(self):
        return self._xRes
    @xRes.setter
    def xRes(self, xRes):
        self._xRes = xRes


    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, image):
        self._image = image


    # Generate the initial window, an array of coords that represent screen pixels.
    def generateWindow(self):

        print("Generating Window")
        self._window = np.ones((self._yRes, self._xRes, 4))

        windowWidth = 2 * math.tan(self._fov / 2)
        distanceBetweenPoints = windowWidth / (self._xRes-1)
        leftMostX = 0 - (windowWidth / 2)
        topMostY  = distanceBetweenPoints * ((self._yRes / 2) - .5)

        # Create window with Eye at 0,0,0
        for row in range(self._yRes):
            for col in range(self._xRes):
                self._window[row][col][2] = -1 # Window is -1 z away from the Eye
                self._window[row][col][0] = leftMostX + (col * distanceBetweenPoints) # x
                self._window[row][col][1] = topMostY - (row * distanceBetweenPoints) # y
        return


    # Transform the camera to the correct location
    def positionCamera(self):

        lookAt_view = self._lookAt - self._lookFrom # Center the lookFrom point to 0,0,0
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
        print("Window Before Rotation: ")
        print(self._window)

        for row in range(self._yRes):
            for col in range(self._xRes):
                self._window[row][col] = combinedRotation.dot(self._window[row][col]) # rotate
                self._window[row][col] = np.add(self._window[row][col], self._lookFrom) # translate
                self._window[row][col][3] = 1 # reset w to 1

        print("Window After Rotation: ")
        print(self._window)

        self._eye = self._lookFrom
        print("eye: " + str(self._eye))

        return




    def renderScene(self, scene):














        return self._image
