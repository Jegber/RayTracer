import Camera, Object

class Scene:

    def __init__(self, directionToLight=[1,0,0], directionalLightColor=[1,1,1],
                 ambientLight = [.1, .1, .1], camera=Camera.Camera()):
        #self._camera = Camera.Camera((0,0,0), (0,0,1), (0,1,0), 28, 4, 3)
        self.camera = camera
        self.bgColor = [.2 * 255, .2 * 255, .2 * 255]
        self.ambientLight = ambientLight
        self.objects = []
        self.directionToLight = directionToLight
        self.directionToLight.append(1)
        self.directionalLightColor = directionalLightColor


    def addObject(self, renderable):
        self.objects.append(renderable)
        print("adding object. Total now: " + str(len(self.objects)))


    def render(self):
        return self.camera.renderScene(self)
