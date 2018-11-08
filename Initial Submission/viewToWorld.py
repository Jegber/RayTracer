import numpy as np
import math



v = np.array([0, 10, 0, 1])
radians = np.deg2rad(90)
xRotation = np.matrix( [ [1, 0, 0,  0],
                         [0, np.cos(radians), -np.sin(radians),  0],
                         [0, np.sin(radians), np.cos(radians),  0],
                         [0, 0, 0,  1] ] )
print(xRotation.dot(v))


v = np.array([0, 0, 10, 1])
radians = np.deg2rad(90)
yRotation = np.matrix( [ [np.cos(radians), 0, np.sin(radians),  0],
                         [0, 1, 0,  0],
                         [-np.sin(radians), 0, np.cos(radians),  0],
                         [0, 0, 0,  1] ] )
print(yRotation.dot(v))





lookAt =   np.array([0, 0, -10])
lookFrom = np.array([0, 0, -1])
newLookAt = lookAt - lookFrom
print(newLookAt)





def angle_between(p1, p2):
    print("Angle between " + str(p1) + "and" + str(p2))
    if (np.array_equal(p1, [0, 0]) or np.array_equal(p2, [0, 0])): return 0
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    #return np.rad2deg((2*np.pi) - ((ang1 - ang2) % (2 * np.pi)))
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))


lookFrom = np.array([0, 0, -1])
lookAt = np.array([0, 0, 1])

yDegree = angle_between([lookFrom[0], lookFrom[2]], [lookAt[0], lookAt[2]]) # xz plane
print(yDegree)
xDegree = angle_between([lookAt[1], lookAt[2]], [lookFrom[1], lookFrom[2]]) # yz plane. LookAt and lookFrom are switched flip the rotation angle.
print(xDegree)
