from graphics import *
from math import *

class Point3D:
    def __init__(self, x, y, z):
        self.coords = [x, y, z]


def matmulvec(i_vec, width, height, focal_length):
    print(i_vec[0], i_vec[1], i_vec[2])
    zFar = 1000
    zNear = 0.1
    w = i_vec[2] + 1
    _x =(i_vec[0] + 1)*width/height * width/2
    _y = (i_vec[1] + 1)*width/height * height/2
    _z = i_vec[2] * (zFar/(zFar - zNear)) - zFar*zNear/(zFar - zNear)
    if w != 0:
        _x /= w
        _y /= w
        _z /= w

    # print(_x, _y, focal_length/2)
    a = Point(_x, _y)

    return a


def TranslateTo2D(Point3, width, height, focal_length):
        res = matmulvec(Point3, width, height, focal_length)
        return res
