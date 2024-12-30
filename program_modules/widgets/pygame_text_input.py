import pygame
import pyperclip
from .pygame_image import PygameImage
from .pygame_text import PygameText
from ..tools.pygame_storage import pygame_storage

class PygameTextInput():
    def __init__(
        self,
        size : tuple,
        coordinates : tuple,
        event : object,
        name : str,
        store_to : str,
        initial_text : str):

        self.name = name
        self.store_to = store_to
        self.initial_text = initial_text
        self.x, self.y = coordinates
        self.width, self.height = size
        self.event = event

        pygame_storage.add_variable({f"{self.name}_text_input_status" : False})

        self.input_text(event)
        self.click_checking(event)
        self.show()

    def show(self):
        if pygame_storage.storage_dict[f"{self.name}_text_input_status"] == False:
            self.input_image = PygameImage(
                coordinates = (self.x, self.y),
                size = (self.width, self.height),
                path = "static/images/input_field.png"
            )

        else:
            self.input_image = PygameImage(
                coordinates = (self.x, self.y),
                size = (self.width, self.height),
                path = "static/images/input_field_selected.png"
            )
        
        self.input_text_lable = PygameText(
            text = pygame_storage.storage_dict[self.store_to],
            font = None,
            font_size = 50,
            x = self.x+10,
            y = self.y+30
        )


    def change_status(self):
        if pygame_storage.storage_dict[f"{self.name}_text_input_status"] == False:
            pygame_storage.storage_dict[f"{self.name}_text_input_status"] = True
            pygame_storage.storage_dict[self.store_to] = ""
            
        else:
            pygame_storage.storage_dict[f"{self.name}_text_input_status"] = False

    def input_text(self, event):
        for pygame_event in event:
            if pygame_storage.storage_dict[f"{self.name}_text_input_status"] == True:
                if pygame_event.type == pygame.KEYDOWN:
                    if pygame_event.key == pygame.K_BACKSPACE:
                        pygame_storage.storage_dict[self.store_to] = pygame_storage.storage_dict[self.store_to][:-1]
                    elif pygame_event.key == 118:
                        pygame_storage.storage_dict[self.store_to] = pyperclip.paste()
                    else:
                        pygame_storage.storage_dict[self.store_to] += pygame_event.unicode

    def click_checking(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for pygame_event in event:
            if mouse_x >= self.x and mouse_x <= self.x + self.width and mouse_y >= self.y and mouse_y <= self.y + self.height:
                if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                    pygame_storage.storage_dict[f"{self.name}_text_input_status"] = False
                    self.change_status()
        
            else:
                if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                    pygame_storage.storage_dict[f"{self.name}_text_input_status"] = True
                    self.change_status()