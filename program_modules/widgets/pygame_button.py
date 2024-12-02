import pygame
from .pygame_image import PygameImage
from .pygame_text import PygameText

#Робим клас для створення кнопки
class PygameButton():
    def __init__(
        self,
        screen : object,
        path : str,
        coordinates : tuple,
        size : tuple,
        event : object,
        function,
        font_size = 20,
        text = None):
        
        #
        self.button_x, self.button_y = coordinates
        self.button_width, self.button_height = size

        #
        self.button_image = PygameImage(screen, path, coordinates, size)
        self.button_text_font = pygame.font.Font(None, font_size)

        #Робим умову для кнопки
        if text != None:
            button_text_x = self.button_x + self.button_width/2 - len(text)*font_size/6
            button_text_y = self.button_y + self.button_height/2 - font_size/4

            #Робим текст для кнопки
            self.button_text = PygameText(
            screen = screen,
            text = text,
            font = None,
            font_size = font_size,
            x = button_text_x,
            y = button_text_y)

        #Робим функцію для натискання кнопки
        self.click_checking(event, function)

    def click_checking(self, event, function):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Робим цикл для натискання кнопки
        for pygame_event in event: 
            if mouse_x >= self.button_x and mouse_x <= self.button_x + self.button_width:
                if mouse_y >= self.button_y and mouse_y <= self.button_y + self.button_height:
                    if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                        function()