import pygame
from ..tools.storage import storage
#Створюємо клас для фото
class PygameImage():
    def __init__(
        self,
        path : str,
        coordinates : tuple,
        size : tuple,
        alpha : int = 255,
        angle : int = 0,
        already_display : bool = True):

        #Робим відображення кнопки
        self.image = storage.storage_dict["ImageContainer"].images[path]
        self.image = pygame.transform.scale(self.image, size)
        self.image.set_alpha(alpha)

        if angle != 0:
            self.image = pygame.transform.rotate(self.image, angle = angle)

        #Робим росташування кнопки
        self.rect = self.image.get_rect()
        self.rect.topleft = coordinates

        if already_display:
            self.display()

    def display(self):
        storage.storage_dict["SCREEN"].blit(self.image, (self.rect.x, self.rect.y))