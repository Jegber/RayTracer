import RayTracer
import Scene, Object, Camera
import random
import numpy as np


camera = Camera.Camera(fov = 56, rayBounces=1)

rt = RayTracer.RayTracer()


scene = Scene.Scene(camera=camera, directionToLight = [1, 1, 1], ambientLight = [.1, .1, .1])

rows = 5
cols = 5

for row in range(rows):
    for col in range(cols):

        xPos = np.interp(col, (0, cols-1), (-1, 1))
        yPos = np.interp(row, (0, rows-1), (-1, 1))
        sphere = Object.Sphere(center=[xPos, yPos, random.uniform(-2, -4)], radius=random.uniform(.1, .4), \
                               diffuse=[random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1)], \
                               specular=[random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1)], \
                               phong=random.uniform(1, 128))
        scene.addObject(sphere)




#Scene 2




rt.renderToFile(scene, 'generatedImages/raytracerTest.ppm')
