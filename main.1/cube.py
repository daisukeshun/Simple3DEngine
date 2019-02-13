import pygame
from pygame import *
from mymath import *
from mesh import *
from math import *



def main():
    W = 1200
    H = 600
    BLACK = (0, 0, 0)
    focal_length = 90
    pygame.init()
    win = pygame.display.set_mode((W, H))
    Camera = [0.0,0.0,0.0,0.0]

    a = mesh('tree01.obj')
    b = mesh('Cube.obj')
    clock = pygame.time.Clock()
    ss = 0
    loop = True
    while loop:
        clock.tick(60)
        for i in pygame.event.get():
                if i.type == pygame.QUIT:
                        loop = False
                elif i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                        loop = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
                Camera[2] -= 0.2
        if keys_pressed[pygame.K_a]:
                Camera[0] += 0.2
                ss -= 3
        if keys_pressed[pygame.K_s]:
                Camera[2] += 0.2
        if keys_pressed[pygame.K_d]:
                Camera[0] -= 0.2
                ss += 3
        pygame.draw.rect(win, BLACK, (0,0, W, H))
        b.meshDraw(win, W, H, focal_length, ss, Camera)
        a.meshDraw(win, W, H, focal_length, ss, Camera)
        # print(Camera)
        pygame.display.update()
main()





