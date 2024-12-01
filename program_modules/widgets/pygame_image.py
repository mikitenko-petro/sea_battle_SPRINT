import pygame
from ..search_path import search_path
#Створюємо клас для фото
class PygameImage():
    def __init__(
        self,
        screen : object,
        path : str,
        coordinates : tuple,
        size : tuple):
    
        #
        self.screen = screen

        #Робим відображення кнопки
        self.image = pygame.image.load(search_path(path))
        self.image = pygame.transform.scale(self.image, size)

        #Робим росташування кнопки
        self.rect = self.image.get_rect()
        self.rect.topleft = coordinates

        self.draw()

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))