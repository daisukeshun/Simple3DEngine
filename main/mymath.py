from graphics import *
from math import *

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        



def matmulvec(i_vec, projM):
    _x = i_vec[0] * projM[0][0] + i_vec[1] * projM[1][0] + i_vec[2] * projM[2][0] + projM[3][0]
    _y = i_vec[0] * projM[0][1] + i_vec[1] * projM[1][1] + i_vec[2] * projM[2][1] + projM[3][1]
    _z = i_vec[0] * projM[0][2] + i_vec[1] * projM[1][2] + i_vec[2] * projM[2][2] + projM[3][2]
    _w = i_vec[0] * projM[0][3] + i_vec[1] * projM[1][3] + i_vec[2] * projM[2][3] + projM[3][3]
    if (_w != 0):
        _x /= _w
        _y /= _w
        _z /= _w
    
    a = Point(_x, _y)

    return a


def TranslateTo2D(Point3, fov, width, height, viewLengh):
        projectMatrix = [[0 for j in range(4)] for i in range(4)]
        projectMatrix[0][0] = width/height*(1/tan(radians(fov/2)))
        projectMatrix[1][1] = 1/tan(radians(fov/2))
        projectMatrix[2][2] = viewLengh/viewLengh - 0.1
        projectMatrix[3][2] = -viewLengh*0.1/viewLengh - 0.1
        projectMatrix[2][3] = 1

        res = matmulvec(Point3, projectMatrix)
        res.x /= 10
        res.y /= 10
        res.x = (res.x + 1) * width/2
        res.y = (res.y + 1) * height/2

        return res
