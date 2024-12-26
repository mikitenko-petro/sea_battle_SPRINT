import pygame
from ..search_path import search_path
#Робимо Текст
class PygameText():
    def __init__(
        self,
        screen : object,
        text : str,
        font_size : int,
        x : int,
        y : int,
        font : str | None = None,
        color : tuple[int, int, int] = (0, 0, 0)):

        self.font = None

        if font == None:
            self.font = font
        else:
            self.font = search_path(font)
        
        #Робим сам текст
        self.button_font = pygame.font.Font(self.font, font_size)
        self.button_text = self.button_font.render(text, True, color)
        screen.blit(self.button_text, (x, y))