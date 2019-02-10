from graphics import *
from math import *

class Point3D:
    def __init__(self, x, y, z):
        self.coords = [x, y, z]


def matmulvec(i_vec, width, height, focal_length):
    print(i_vec[0], i_vec[1], i_vec[2])
    zFar = 1000
    zNear = 0.1
    w = i_vec[2] + 3
    _x =(i_vec[0])* width/height * width/2
    _y = -(i_vec[1]) * height/2
    _z = i_vec[2] * (zFar/(zFar - zNear)) - zFar*zNear/(zFar - zNear)
    if w != 0:
        _x /= w
        _y /= w
        _z /= w


    _x += width/2
    _y += height/2
    # print(_x, _y, focal_length/2)
    a = Point(_x, _y)

    return a


def mmult(i, m):
    o = []
    o.append(i[0] * m[0][0] + i[1]*m[1][0] + i[2]*m[2][0])
    o.append(i[0] * m[0][1] + i[1]*m[1][1] + i[2]*m[2][1])
    o.append(i[0] * m[0][2] + i[1]*m[1][2] + i[2]*m[2][2])
    return o

def TranslateTo2D(Point3, width, height, focal_length):
        res = matmulvec(Point3, width, height, focal_length)
        return res

def rotateX(angle, point):
    angle = radians(angle)
    m = [[1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]]    
    res = mmult(point, m)
    print(res)
    return res


def rotateY(angle, point):
    angle = radians(angle)
    m = [[cos(angle), 0, sin(angle)],
         [0, 1, 0],
         [-sin(angle), 0, cos(angle)]]

    res = mmult(point, m)
    print(res)
    return res
