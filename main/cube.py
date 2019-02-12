import pygame
from mymath import *
from mesh import *
from math import *

W = 1200
H = 600
BLACK = (0,0,0)
focal_length = 90


def main():
    pygame.init()
    win = pygame.display.set_mode((W, H))

    a = mesh('tree01.obj')

    clock = pygame.time.Clock()
    ss = 0
    while True:
        clock.tick(30)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
        pygame.draw.rect(win, BLACK, (0,0, W, H))
        a.meshDraw(win, W, H, focal_length, ss)
        pygame.display.update()

        ss+=1
main()





