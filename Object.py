
class Object(object):

    def __init__(self, color=(255, 0, 0), diffuse = (1, 1, 1),
                       specular = (1, 1, 1), phong = 4):
        self._color = color
        self._diffuse = diffuse
        self._specular = specular
        self._phong = phong


    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color


    @property
    def diffuse(self):
        return self._diffuse
    @diffuse.setter
    def diffuse(self, diffuse):
        self._diffuse = diffuse


    @property
    def specular(self):
        return self._specular
    @specular.setter
    def specular(self, specular):
        self._specular = specular


    @property
    def phong(self):
        return self._phong
    @phong.setter
    def phong(self, phong):
        self._phong = phong




class Sphere(Object):

    def __init__(self, color=(255, 0, 0), diffuse = (1, 1, 1),
                       specular = (1, 1, 1), phong = 4,
                       center=(.35, 0, -.1), radius=.05):
        Object.__init__(self, color, diffuse, specular, phong)
        self._center = center
        self._radius = radius


    @property
    def center(self):
        return self._center
    @center.setter
    def center(self, center):
        self._center = center


    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, radius):
        self._radius = radius




class Triangle(Object):

    def __init__(self, color=(255, 0, 0), diffuse = (1, 1, 1),
                       specular = (1, 1, 1), phong = 4,
                       vertex1=(.3, -.3, -.4),
                       vertex2=(0, .3, -.1),
                       vertex3=(-.3, -.3, .2) ):
        Object.__init__(self, color, diffuse, specular, phong)
        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._vertex3 = vertex3


    @property
    def vertices(self):
        return self._vertices
    @vertices.setter
    def vertices(self, vertex1, vertex2, vertex3):
        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._vertex3 = vertex3
