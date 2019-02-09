from graphics import *
from math import *

class Point3D:
    def __init__(self, string):
        self = string.split()

class Triangle3D:
    def __init__(self, p1, p2, p3, width, height, focal_length):
        self.points = [0, 0, 0]
        self.points[0] = p1
        self.points[1] = p2
        self.points[2] = p3

    def draw3D(self, graphic):
        p = self.points
        Line(Point(p[0][0], p[0][1]), Point(p[1][0], p[1][1])).draw(graphic)
        Line(Point(p[1][0], p[1][1]), Point(p[2][0], p[2][1])).draw(graphic)
        Line(Point(p[2][0], p[2][1]), Point(p[0][0], p[0][1])).draw(graphic)

    def drawPoints(self, graphic):
        p = self.points
        for i in p:
            i.draw(graphic)
            print('Triangle')


class Square3D:
    def __init__(self, p1, p2, p3, p4, width, height,zFar, zNear):
        self.points = [0, 0, 0, 0]
        self.points[0] = p1
        self.points[1] = p2
        self.points[2] = p3
        self.points[3] = p4
        # print(self.points)

    def draw3D(self, graphic):
        p = self.points

        Line(Point(p[0][0], p[0][1]), Point(p[1][0], p[1][1])).draw(graphic)
        Line(Point(p[1][0], p[1][1]), Point(p[2][0], p[2][1])).draw(graphic)
        Line(Point(p[2][0], p[2][1]), Point(p[3][0], p[3][1])).draw(graphic)
        Line(Point(p[3][0], p[3][1]), Point(p[0][0], p[0][1])).draw(graphic)

    def drawPoints(self, graphic):
        p = self.points
        for i in p:
            i.draw(graphic)


def TranslateTo2D(face, fov, width, height, zFar, zNear):
        for i in face.points:
            w = i[2]
            i[0] = i[0] * width/height * (1/tan(radians(fov/2)))
            i[1] = i[1] * 1/tan(radians(fov/2))
            i[2] = i[2] * (zFar/(zFar - zNear)) - zFar*zNear/(zFar - zNear)

            if w != 0:
                i[0] /= w
                i[1] /= w
                i[2] /= w
            print(i[0], i[1], i[2])
        return face


def RotateX(angle, vector):
    angle = radians(angle)
    cosine = cos(angle)
    sine = sin(angle)
    y = vector[1] * cosine - vector[2] * sine
    z = -vector[1] * sine + vector[2] * cosine
    vector[1] = y
    vector[2] = z
    print(vector)
    return vector


def RotateY(angle, vector):
    angle = radians(angle)
    cosine = cos(angle)
    sine = sin(angle)
    x = vector[0] * cosine + vector[2] * sine
    z = -vector[0] * sine + vector[2] * cosine
    vector[0] = x
    vector[2] = z
    print(vector)
    return vector

