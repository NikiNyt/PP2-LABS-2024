import pygame
import os
from math import *
import datetime

pygame.init()

screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

hand1 = pygame.image.load('hand1.png')
hand2 = pygame.image.load('hand2.png')
base = pygame.image.load('mickeyclock.png')

base = pygame.transform.scale(base, (700, 700))

def rotate_and_blit(fixed, origin, pic, angle, screen):
    pic_rect = pic.get_rect(topleft = (fixed[0] - origin[0], fixed[1] - origin[1]))
    offset = pygame.math.Vector2(fixed) - pic_rect.center

    rotated_offset = offset.rotate(-angle)
    rotated_pic_center = (fixed[0] - rotated_offset.x, fixed[1] - rotated_offset.y)

    rotated_pic = pygame.transform.rotate(pic, angle)
    rotated_pic_rect = rotated_pic.get_rect(center = rotated_pic_center)

    screen.blit(rotated_pic, rotated_pic_rect)


fixed = (339, 350)
origin_s = (12, 153)
origin_m = (12, 170)

run = True 
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    time = datetime.datetime.now()
    second = time.second
    minute = time.minute

    screen.blit(base, (0, 0))
    rotate_and_blit(fixed, origin_s, hand1, -second * 6 + 57, screen)
    rotate_and_blit(fixed, origin_m, hand2, -((minute + second/60) * 6) + 43, screen)

    pygame.display.update()
    clock.tick(60)