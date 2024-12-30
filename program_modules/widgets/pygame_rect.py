import pygame
from .pygame_hitbox import PygameHitBox
from ..tools.pygame_storage import pygame_storage

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

        if pygame_storage.storage_dict["debug"]:
            pygame.draw.rect(pygame_storage.storage_dict["SCREEN"], debug_color, self, 2)
            
    def draw(self):
        pygame.draw.rect(pygame_storage.storage_dict["SCREEN"], self.color,self, 2)