import numpy as np
import math
import Ray
import random
from tqdm import tqdm
from multiprocessing import Pool

class Camera:

    def __init__(self, lookAt=np.array([0,0,-1]), lookFrom=np.array([0,0,0]),
                lookUp=np.array([0,1,0]), fov=56, xRes=501, yRes=501, aa=0,
                rayBounces = 0 ):
        self.lookAt = np.array([lookAt[0], lookAt[1], lookAt[2], 1])
        self.lookFrom = np.array([lookFrom[0], lookFrom[1], lookFrom[2], 1])
        self.lookUp = np.array([lookUp[0], lookUp[1], lookUp[2], 1])
        self.fov = fov
        self.xRes = xRes
        self.yRes = yRes
        self.image = np.full((self.yRes, self.xRes, 3), 150)
        self.window = None
        self.eye = np.array([0,0,0,1])
        self.aa = aa # anti-aliasing level based on random jitter
        self.rayBounces = rayBounces
        self.generateWindow() # Generate the window's pixel center points
        self.positionCamera() # Move the camera into position



    # Generate the initial window, an array of coords that represent screen pixels.
    def generateWindow(self):

        print("Generating Window")
        self.window = np.ones((self.yRes, self.xRes, 4))

        windowWidth = 2 * math.tan(np.deg2rad(self.fov) / 2)
        print("windowWidth: " + str(windowWidth))
        distanceBetweenPoints = windowWidth / (self.xRes-1)
        leftMostX = 0 - (windowWidth / 2)
        topMostY  = distanceBetweenPoints * ((self.yRes / 2) - .5)

        # Create window with Eye at 0,0,0
        for row in range(self.yRes):
            for col in range(self.xRes):
                yJig = self.aa * random.uniform(-distanceBetweenPoints, distanceBetweenPoints)
                xJig = self.aa * random.uniform(-distanceBetweenPoints, distanceBetweenPoints)
                self.window[row][col][2] = -1 # Window is -1 z away from the Eye
                self.window[row][col][0] = leftMostX + (col * distanceBetweenPoints) + xJig# x
                self.window[row][col][1] = topMostY - (row * distanceBetweenPoints) + yJig# y
        return


    # Transform the camera to the correct location
    def positionCamera(self):

        lookAtview = self.lookAt - self.lookFrom # Center the lookFrom point to 0,0,0
        camForward = np.array([0,0,-1])

        def anglebetween(p1, p2):
            if (np.array_equal(p1, [0, 0]) or np.array_equal(p2, [0, 0])): return 0
            ang1 = np.arctan2(*p1[::-1])
            ang2 = np.arctan2(*p2[::-1])
            return (ang1 - ang2) % (2 * np.pi)

        yRad = anglebetween([camForward[0], camForward[2]], [lookAtview[0], lookAtview[2]]) # xz plane
        xRad = anglebetween([lookAtview[1], lookAtview[2]], [camForward[1], camForward[2]]) # yz plane. LookAt and lookFrom are switched flip the rotation angle.

        xRotation = np.matrix( [ [1, 0, 0,  0],
                                 [0, np.cos(xRad), -np.sin(xRad),  0],
                                 [0, np.sin(xRad), np.cos(xRad),  0],
                                 [0, 0, 0,  1] ] )
        yRotation = np.matrix( [ [np.cos(yRad), 0, np.sin(yRad),  0],
                                 [0, 1, 0,  0],
                                 [-np.sin(yRad), 0, np.cos(yRad),  0],
                                 [0, 0, 0,  1] ] )

        combinedRotation = yRotation * xRotation

        for row in range(self.yRes):
            for col in range(self.xRes):
                self.window[row][col] = combinedRotation.dot(self.window[row][col]) # rotate
                self.window[row][col] = np.add(self.window[row][col], self.lookFrom) # translate
                self.window[row][col][3] = 1 # reset w to 1


        self.eye = self.lookFrom

        return



    def renderScene(self, scene):
        # Cast Rays

        for row in range(self.yRes):
            for col in range(self.xRes):
                #print()
                #print(str(self.window[row][col]) + "   ")
                self.renderPixel(scene, row, col)

            #print("\n")

        return self.image



    def renderPixel(self, scene, row, col):
        #print()
        #print("Rendering ", row, col)
        primaryRay = Ray.PrimaryRay(self.eye, self.window[row][col],
                                    bouncesLeft = self.rayBounces)
        self.image[row][col] = primaryRay.getColor(scene)
