import pygame
from .pygame_hitbox import PygameHitBox
from ..pygame_storage import pygame_storage

class PygameRect(PygameHitBox, pygame.Rect):
    def __init__(
            self,
            coordinates,
            size,
            color : tuple | None = None,
            debug_color : tuple = (0,255,0),
            screen : object | None = None):
        
        PygameHitBox.__init__(self, coordinates, size)
        pygame.Rect.__init__(self, self.x, self.y, self.width, self.height)

        self.color = color
        self.screen = screen

        if pygame_storage.storage_dict["debug"] and screen:
            pygame.draw.rect(screen, debug_color, self, 2)
            
    def draw(self):
        pygame.draw.rect(self.screen, self.color,self, 2)