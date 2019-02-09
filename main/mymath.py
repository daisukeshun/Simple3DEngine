from graphics import *
from math import *

class Point3D:
    def __init__(self, x, y, z):
        self.coords = [x, y, z]


def matmulvec(i_vec, width, height, focal_length):
    zFar = 1000
    zNear = 0.1
    w = i_vec[2]
    _x =(i_vec[0] * width/height * focal_length/2) * width/2
    _y = (i_vec[1] * width/height * focal_length/2) * height/2
    _z = i_vec[2] * (zFar/(zFar - zNear)) - zFar*zNear/(zFar - zNear)
    if w != 0:
        _x /= w
        _y /= w
    #     _z /= w


    # _x *= 0.5
    # _y *= 0.5
    # _z *= 0.5
    # print(_x, _y, fov/i_vec[2])
    a = Point(_x, _y)

    return a


def TranslateTo2D(Point3, width, height, focal_length):
        res = matmulvec(Point3, width, height, focal_length)
        return res
