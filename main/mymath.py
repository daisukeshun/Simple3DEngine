from graphics import *
from math import *

class Point3D:
    def __init__(self, string):
        self = string.split()

def matmulvec(i_vec, width, height, focal_length):
    _x =(1 + i_vec[0] * focal_length/(i_vec[2]+1)) + width/2
    _y =-(1 + i_vec[1] * focal_length/(i_vec[2]+1)) + height/2

    # print(_x, _y, focal_length/i_vec[2])
    a = Point(_x, _y)

    return a


def TranslateTo2D(Point3, width, height, focal_length):
        res = matmulvec(Point3, width, height, focal_length)
        return res
