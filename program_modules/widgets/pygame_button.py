import pygame
from .pygame_image import PygameImage

class PygameButton():
    def __init__(self, screen, path, coordinates, size, event):
        self.button_image = PygameImage(screen, path, coordinates, size)   
        self.click_checking(event)
    def click_checking(self, event):
        #mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(2232)
                
