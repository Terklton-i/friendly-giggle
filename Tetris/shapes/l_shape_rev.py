import pygame
from colors import *

class L_shape_rev(object):
    def __init__(self, one, two, three, tail, facing):

        self.one = one
        self.two = two
        self.three = three
        self.tail = tail
        self.facing = facing

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.one)
        pygame.draw.rect(screen, YELLOW, self.two)
        pygame.draw.rect(screen, YELLOW, self.three)
        pygame.draw.rect(screen, YELLOW, self.tail)
