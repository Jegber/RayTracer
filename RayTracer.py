import Scene
import generatePPM as ppm

class RayTracer:

    def __init__(self):
        pass

    # Renders a scene to a file.
    def renderToFile(self, scene, filepath):
        ppm.RGBNumpyArrayToPPMFile(scene.render(), filepath)
