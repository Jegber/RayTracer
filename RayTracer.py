import Scene
import generatePPM as ppm

class RayTracer:

    testRGBArray = [[(255,0,0), (0,255,0), (0,0,255)]]

    def __init__(self):
        self.scene = Scene.Scene()
        pass


    # Renders a scene to a file.
    def renderToFile(self, scene, filepath):
        ppm.RGBArrayToPPMFile(self.testRGBArray, filepath)


    def setScene(self, scene):
        self.scene = scene
