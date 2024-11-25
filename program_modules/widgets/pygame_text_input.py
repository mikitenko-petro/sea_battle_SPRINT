import pygame
from .pygame_button import PygameButton
from .pygame_image import PygameImage
from .pygame_text import PygameText

class PygameTextInput():
    def __init__(self, size, coordinates, event, screen, pygame_storage):
        self.screen = screen
        self.pygame_storage = pygame_storage
        self.x, self.y = coordinates
        self.width, self.height = size
        self.pygame_storage.add_variable({"status" : "not selected"})

        self.click_checking(event)
        self.show()

    def click_checking(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for pygame_event in event: 
            if mouse_x >= self.x and mouse_x <= self.x + self.width:
                if mouse_y >= self.y and mouse_y <= self.y + self.height:
                    if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                        self.change_status()

    def change_status(self):
        self.pygame_storage.storage_dict["status"] = "selected"

    def show(self):
        if self.pygame_storage.storage_dict["status"] == "not selected":
            self.input_image = PygameImage(
            screen = self.screen,
            coordinates = (self.x, self.y),
            size = (self.width, self.height),
            path = "static/images/input_field.png")

            self.input_text = PygameText(
            screen = self.screen,
            text = "Enter ip adress",
            font = None,
            font_size = 50,
            x = self.x+10,
            y = self.y+30)
        else:
            self.input_image = PygameImage(
            screen = self.screen,
            coordinates = (self.x, self.y),
            size = (self.width, self.height),
            path = "static/images/input_field_selected.png")

            self.input_text = PygameText(
            screen = self.screen,
            text = "",
            font = None,
            font_size = 50,
            x = self.x+10,
            y = self.y+30)
        