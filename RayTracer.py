import Scene
import generatePPM as ppm

class RayTracer:

    def __init__(self):
        self._scene = Scene.Scene()
        pass

    @property
    def scene(self):
        return self._scene
    @scene.setter
    def lookFrom(self, scene):
        self._scene = scene

    # Renders a scene to a file.
    def renderToFile(self, scene, filepath):
        ppm.RGBNumpyArrayToPPMFile(scene.render(), filepath)
