import RayTracer
import Scene, Object, Camera
import random, requests
import numpy as np


camera = Camera.Camera(fov = 56, rayBounces=1)

rt = RayTracer.RayTracer()


def makeArt(title):

    scene = Scene.Scene(camera=camera, directionToLight = [1, 1, 1], ambientLight = [.1, .1, .1])


    rows = random.randint(3, 10)
    cols = rows

    for row in range(rows):
        for col in range(cols):

            xPos = np.interp(col, (0, cols-1), (-1, 1))
            yPos = np.interp(row, (0, rows-1), (-1, 1))
            sphere = Object.Sphere(center=[xPos, yPos, random.uniform(-2, -4)], radius=random.uniform(.1, .4), \
                                diffuse=[random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1)], \
                                specular=[random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1)], \
                                phong=random.uniform(1, 128))
            scene.addObject(sphere)

    destination = "generatedImages/" + title +".ppm"
    rt.renderToFile(scene, destination)



words = requests.get("http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain").content.splitlines()
x = 0

def generateRandomWord():
    return str(words[random.randint(0, len(words))]).replace("'b'","").replace("b'", "").replace("'", "").capitalize()

def generateTitle(numWords=2):
    title = ""
    for i in range(numWords):
        title += generateRandomWord()
        if i < numWords-1: title += " "
    return title



for i in range(10):
    makeArt(generateTitle())
