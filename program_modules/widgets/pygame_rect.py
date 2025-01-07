import pygame
from .pygame_hitbox import PygameHitBox
from ..tools.storage import storage

class PygameRect(PygameHitBox, pygame.Rect):
    def __init__(
            self,
            coordinates,
            size,
            color : tuple | None = None,
            debug_color : tuple = (0,255,0)):
        
        PygameHitBox.__init__(self, coordinates, size)
        pygame.Rect.__init__(self, self.x, self.y, self.width, self.height)

        self.color = color

        if storage.storage_dict["debug"]:
            pygame.draw.rect(storage.storage_dict["SCREEN"], debug_color, self, 2)
            
    def draw(self, border):
        pygame.draw.rect(storage.storage_dict["SCREEN"], self.color, self, border)