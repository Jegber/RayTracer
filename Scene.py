import Camera

class Scene:

    def __init__(self):
        self.camera = Camera.Camera((0,0,0), (0,0,1), (0,1,0), 28, 16, 9)


    def setCamera(self, camera):
        self.camera = camera
