import pygame
from ..tools.search_path import search_path
from ..tools.pygame_storage import pygame_storage
#Створюємо клас для фото
class PygameImage():
    def __init__(
        self,
        screen : object,
        path : str,
        coordinates : tuple,
        size : tuple,
        angle : int = 0,
        already_display : bool = True):

        #
        self.screen = screen

        #Робим відображення кнопки
        self.image = pygame_storage.storage_dict["GAME"].image_container.images[path]
        self.image = pygame.transform.scale(self.image, size)

        if angle != 0:
            self.image = pygame.transform.rotate(self.image, angle = angle)

        #Робим росташування кнопки
        self.rect = self.image.get_rect()
        self.rect.topleft = coordinates

        if already_display:
            self.display()

    def display(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))