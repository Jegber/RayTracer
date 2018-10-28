import numpy as np


class Camera:

    def __init__(self, lookAt, lookFrom, lookUp, fov, xRes, yRes):
        self._lookAt = lookAt
        self._lookFrom = lookFrom
        self._lookUp = lookUp
        self._fov = fov
        self._xRes = xRes
        self._yRes = yRes
        self._image = np.full((self._yRes, self._xRes, 3), 150)


    @property
    def lookAt(self):
        return self._lookAt
    @lookAt.setter
    def lookAt(self, lookAt):
        self._lookAt = lookAt


    @property
    def lookFrom(self):
        return self._lookFrom
    @lookFrom.setter
    def lookFrom(self, lookFrom):
        self._lookFrom = lookFrom


    @property
    def lookUp(self):
        return self._lookUp
    @lookUp.setter
    def lookUp(self, lookUp):
        self._lookUp = lookUp


    @property
    def fov(self):
        return self._fov
    @fov.setter
    def fov(self, fov):
        self._fov = fov


    @property
    def xRes(self):
        return self._xRes
    @xRes.setter
    def xRes(self, xRes):
        self._xRes = xRes


    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, image):
        self._image = image
