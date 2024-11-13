import pygame
from .pygame_image import PygameImage

class PygameButton():
    def __init__(self, screen, path, size):
        button_image = PygameImage(screen, path, size)        
    def click_checking(self, event):
        #mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(2232)
                
