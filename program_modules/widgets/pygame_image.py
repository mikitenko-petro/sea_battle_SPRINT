import pygame
from ..search_path import search_path

class PygameImage():
    def __init__(self, screen, path, coordinates, size):
        self.screen = screen

        self.image = pygame.image.load(search_path(path))
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.rect.topleft = coordinates

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))