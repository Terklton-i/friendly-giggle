import pygame
from colors import *

class Line(object):
    def __init__(self, one, two, three, four, facing):

        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.facing = facing

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.one)
        pygame.draw.rect(screen, WHITE, self.two)
        pygame.draw.rect(screen, WHITE, self.three)
        pygame.draw.rect(screen, WHITE, self.four)
