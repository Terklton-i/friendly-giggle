import pygame
from colors import *

class Square(object):
    def __init__(self, tl, tr, bl, br):

        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.bl)
        pygame.draw.rect(screen, RED, self.br)
        pygame.draw.rect(screen, RED, self.tl)
        pygame.draw.rect(screen, RED, self.tr)
