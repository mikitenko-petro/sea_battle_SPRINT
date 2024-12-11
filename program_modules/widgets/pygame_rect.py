import pygame
from .pygame_hitbox import PygameHitBox


class PygameRect(PygameHitBox, pygame.Rect):
    def __init__(self, coordinates, size):
        PygameHitBox.__init__(self, coordinates, size)
        
        pygame.Rect.__init__(self, self.x, self.y, self.width, self.height)