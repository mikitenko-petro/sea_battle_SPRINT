import pygame
from .pygame_image import PygameImage
from .pygame_text import PygameText
from .pygame_hitbox import PygameHitBox

#Робим клас для створення кнопки
class PygameButton(PygameHitBox):
    def __init__(
        self,
        coordinates : tuple,
        size : tuple,
        event : object,
        function : object,
        font_size = 20,
        font : str | None = None,
        text : str | None = None,
        path : str | None = None):

        #
        PygameHitBox.__init__(self, coordinates, size)

        #
        if path != None:
            self.button_image = PygameImage(
                path = path,
                coordinates = coordinates,
                size = size
            )

        #Робим умову для кнопки
        if text != None:
            self.button_text_font = pygame.font.Font(None, font_size)
            button_text_x = self.x + self.width/2 - len(text)*font_size/6
            button_text_y = self.y + self.height/2 - font_size/4

            #Робим текст для кнопки
            self.button_text = PygameText(
                text = text,
                font = font,
                font_size = font_size,
                x = button_text_x,
                y = button_text_y
            )

        #Робим функцію для натискання кнопки
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Робим цикл для натискання кнопки
        for pygame_event in event: 
            if mouse_x >= self.x and mouse_x <= self.x + self.width:
                if mouse_y >= self.y and mouse_y <= self.y + self.height:
                    if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                        function()