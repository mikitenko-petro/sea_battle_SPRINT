import pygame
from .pygame_image import PygameImage
from .pygame_text import PygameText

class PygameButton():
    def __init__(self, screen, path, coordinates, size, event, function, text = None):
        self.button_image = PygameImage(screen, path, coordinates, size)
        self.button_x, self.button_y = coordinates
        self.button_width, self.button_height = size

        button_x = self.button_x + self.button_width/2
        button_y = self.button_y + self.button_height/2

        self.button_text = PygameText(screen, text, button_x, button_y)

        self.click_checking(event, function)

    def click_checking(self, event, function):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for pygame_event in event: 
            if mouse_x >= self.button_x and mouse_x <= self.button_x + self.button_width:
                if mouse_y >= self.button_y and mouse_y <= self.button_y + self.button_height:
                    if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                        function()