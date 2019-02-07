from graphics import *
from math import *

class Point3D:
    def __init__(self, string):
        self = string.split()
        



def matmulvec(i_vec, focal_length, width, height):

    _x = i_vec[0] * focal_length/i_vec[2] + width/2
    _y = i_vec[1] * focal_length/i_vec[2] + height/2
    
    _x *= 0.1
    _y *= 0.1
    _x += 200
    _y += 200


    a = Point(_x, _y)

    return a


def TranslateTo2D(Point3, focal_length, width, height):
        res = matmulvec(Point3, focal_length, width, height)
        return res
