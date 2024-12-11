from ...widgets.pygame_rect import PygameRect
from ...pygame_storage import pygame_storage
import pygame

class Collision():
    def __init__(self, screen, coordinates, size, type):
        self.rect = PygameRect(coordinates, size)

        if pygame_storage.storage_dict["debug"] == True:
            pygame.draw.rect(screen, (0, 255 ,0), self.rect, 2)

        self.type = type