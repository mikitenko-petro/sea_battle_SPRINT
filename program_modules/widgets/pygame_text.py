import pygame
from ..tools.storage import storage
from ..tools.search_path import search_path

class PygameText():
    def __init__(
        self,
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

        self.button_font = pygame.font.Font(self.font, font_size)
        self.button_text = self.button_font.render(str(text), True, color)
        storage.storage_dict["SCREEN"].blit(self.button_text, (x, y))