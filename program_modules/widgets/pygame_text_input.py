import pygame
import pyperclip
from .pygame_image import PygameImage
from .pygame_text import PygameText
from ..tools.storage import storage

#Робимо клас для створення вводу тексту
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

        storage.add_variable({f"{self.name}_text_input_status" : False})

        #Указуємо змінні які будемо використовувати
        self.input_text(event)
        self.click_checking(event)
        self.show()

    #Робимо саму кнопку вводу тексту
    def show(self):
        if storage.storage_dict[f"{self.name}_text_input_status"] == False:
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
        
        #Робимо текст для кнопки
        self.input_text_lable = PygameText(
            text = storage.storage_dict[self.store_to],
            font = None,
            font_size = 50,
            x = self.x+10,
            y = self.y+30
        )

    def change_status(self):
        if storage.storage_dict[f"{self.name}_text_input_status"] == False:
            storage.storage_dict[f"{self.name}_text_input_status"] = True
            storage.storage_dict[self.store_to] = ""
            
        else:
            storage.storage_dict[f"{self.name}_text_input_status"] = False

    #Робимо метод кнопку вводу тексту
    def input_text(self, event):
        for pygame_event in event:
            if storage.storage_dict[f"{self.name}_text_input_status"] == True:
                if pygame_event.type == pygame.KEYDOWN:
                    if pygame_event.key == pygame.K_BACKSPACE:
                        storage.storage_dict[self.store_to] = storage.storage_dict[self.store_to][:-1]
                    elif pygame_event.key == 118:
                        storage.storage_dict[self.store_to] = pyperclip.paste()
                    else:
                        storage.storage_dict[self.store_to] += pygame_event.unicode

    #Робимо метод для натискання миші по кнопці
    def click_checking(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Робимо функцію для натискання миші по кнопці
        for pygame_event in event:
            if mouse_x >= self.x and mouse_x <= self.x + self.width and mouse_y >= self.y and mouse_y <= self.y + self.height:
                if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                    storage.storage_dict[f"{self.name}_text_input_status"] = False
                    self.change_status()
        
            else:
                if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                    storage.storage_dict[f"{self.name}_text_input_status"] = True
                    self.change_status()