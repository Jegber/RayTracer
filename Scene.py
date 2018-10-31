import Camera, Object

class Scene:

    def __init__(self):
        #self._camera = Camera.Camera((0,0,0), (0,0,1), (0,1,0), 28, 4, 3)
        self._camera = Camera.Camera()
        self._bgColor = [0, 0, 0]
        self._ambientLight = (.1, .1, .1)
        self._objects = {}


    @property
    def camera(self):
        return self._camera
    @camera.setter
    def camera(self, camera):
        self._camera = camera


    @property
    def bgColor(self):
        return self._bgColor
    @bgColor.setter
    def bgColor(self, bgColor):
        self._bgColor = bgColor


    @property
    def ambientLight(self):
        return self._ambientLight
    @ambientLight.setter
    def ambientLight(self, ambientLight):
        self._ambientLight = ambientLight


    @property
    def objects(self):
        return self._objects
    @objects.setter
    def objects(self, objects):
        self._objects = objects


    def addObject(self, object):
        self._objects.add(object)


    def render(self):
        return self._camera.renderScene(self)
