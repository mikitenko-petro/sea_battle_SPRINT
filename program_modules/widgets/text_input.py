import pygame
from .pygame_button import PygameButton
from .pygame_image import PygameImage
from .pygame_text import PygameText
from ..search_path import search_path

class TextInput():
    def __init__(self, size, coordinates, event, screen):
        self.screen = screen
        self.x, self.y = coordinates
        self.width, self.height = size
        self.status = ""

        if self.status == "":
            self.input_image = PygameImage(screen = screen, coordinates = coordinates, size = size, path = "static/images/input_field.png")
            self.input_text = PygameText(screen = screen, text = "Enter ip adress", font = None, font_size = 50, x = self.x+10, y = self.y+30)
        else:
            self.input_image = PygameImage(screen = self.screen, coordinates = (self.x, self.y), size = (self.width, self.height), path = "static/images/input_field_selected.png")
            self.input_text = PygameText(screen = self.screen, text = "", font = None, font_size = 50, x = self.x+10, y = self.y+30)

        self.click_checking(event)

    def click_checking(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for pygame_event in event: 
            if mouse_x >= self.x and mouse_x <= self.x + self.width:
                if mouse_y >= self.y and mouse_y <= self.y + self.height:
                    if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                        self.change_status()

    def change_status(self):
        self.status = "selected"
        