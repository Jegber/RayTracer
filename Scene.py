import Camera, Object

class Scene:

    def __init__(self):
        #self._camera = Camera.Camera((0,0,0), (0,0,1), (0,1,0), 28, 4, 3)
        self.camera = Camera.Camera()
        self.bgColor = [0, 0, 0]
        self.ambientLight = (.1, .1, .1)
        self.objects = []


    def addObject(self, renderable):
        self.objects.append(renderable)
        print("adding object. Total now: " + str(len(self.objects)))


    def render(self):
        return self.camera.renderScene(self)
