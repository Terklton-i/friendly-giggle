import pygame
from colors import *

class T_shape(object):
    def __init__(self, one, two, three, tail, facing):

        self.one = one
        self.two = two
        self.three = three
        self.tail = tail
        self.facing = facing

    def draw(self, screen):
        pygame.draw.rect(screen, PURPLE, self.one)
        pygame.draw.rect(screen, PURPLE, self.two)
        pygame.draw.rect(screen, PURPLE, self.three)
        pygame.draw.rect(screen, PURPLE, self.tail)
