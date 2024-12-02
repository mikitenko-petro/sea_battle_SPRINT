import pygame
import pyperclip
from .pygame_button import PygameButton
from .pygame_image import PygameImage
from .pygame_text import PygameText

#Робимо клас для створення вводу тексту
class PygameTextInput():
    def __init__(
        self,
        size : tuple,
        coordinates : tuple,
        event : object,
        screen : object,
        pygame_storage : object,
        name : str,
        store_to : str,
        initial_text : str
        ):
        
        self.name = name
        self.store_to = store_to
        self.initial_text = initial_text
        self.screen = screen
        self.pygame_storage = pygame_storage
        self.x, self.y = coordinates
        self.width, self.height = size
        self.event = event

        #Робим текст який буде змінюватись при натисканні
        self.pygame_storage.add_variable({f"{self.name}_text_input" : initial_text})
        self.pygame_storage.add_variable({f"{self.name}_text_input_status" : False})

        #Указуємо змінні які будемо використовувати
        self.input_text(event)
        self.click_checking(event)
        self.show()

    #Робимо саму кнопку вводу тексту
    def show(self):
        if self.pygame_storage.storage_dict[f"{self.name}_text_input_status"] == False:
            self.input_image = PygameImage(
            screen = self.screen,
            coordinates = (self.x, self.y),
            size = (self.width, self.height),
            path = "static/images/input_field.png")

        else:
            self.input_image = PygameImage(
            screen = self.screen,
            coordinates = (self.x, self.y),
            size = (self.width, self.height),
            path = "static/images/input_field_selected.png")
        
        #Робимо текст для кнопки
        self.input_text_lable = PygameText(
        screen = self.screen,
        text = self.pygame_storage.storage_dict[f"{self.name}_text_input"],
        font = None,
        font_size = 50,
        x = self.x+10,
        y = self.y+30)

        #Робимо кнопку для  піддтвердження
        self.apply_button = PygameButton(
        screen = self.screen,
        event = self.event,
        coordinates = (self.x + self.width + 10, self.y),
        size = (self.width/4, self.height),
        path = "static/images/apply_button.png",
        function = lambda: self.apply())
    
    #Робим функцію для заміни тексту на строку вводу
    def change_status(self):
        if self.pygame_storage.storage_dict[f"{self.name}_text_input_status"] == False:
            self.pygame_storage.storage_dict[f"{self.name}_text_input_status"] = True
            self.pygame_storage.storage_dict[f"{self.name}_text_input"] = ""
        else:
            self.pygame_storage.storage_dict[f"{self.name}_text_input_status"] = False
            self.pygame_storage.storage_dict[f"{self.name}_text_input"] = self.initial_text

    #Робимо метод кнопку вводу тексту
    def input_text(self, event):
        for pygame_event in event:
            if self.pygame_storage.storage_dict[f"{self.name}_text_input_status"] == True:
                if pygame_event.type == pygame.KEYDOWN:
                    if pygame_event.key == pygame.K_BACKSPACE:
                        self.pygame_storage.storage_dict[f"{self.name}_text_input"] = self.pygame_storage.storage_dict[f"{self.name}_text_input"][:-1]
                    elif pygame_event.key == 118:
                        self.pygame_storage.storage_dict[f"{self.name}_text_input"] = pyperclip.paste()
                    else:
                        self.pygame_storage.storage_dict[f"{self.name}_text_input"] += pygame_event.unicode

    #Робимо метод для піддтвердження
    def apply(self):
        if self.pygame_storage.storage_dict[f"{self.name}_text_input"] != "":
            self.pygame_storage.storage_dict[self.store_to] = self.pygame_storage.storage_dict[f"{self.name}_text_input"]
            self.change_status()

    #Робимо метод для натискання миші по кнопці
    def click_checking(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Робимо функцію для натискання миші по кнопці
        for pygame_event in event:
            if self.pygame_storage.storage_dict[f"{self.name}_text_input_status"] == False:
                if mouse_x >= self.x and mouse_x <= self.x + self.width:
                    if mouse_y >= self.y and mouse_y <= self.y + self.height:
                        if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                            self.change_status()