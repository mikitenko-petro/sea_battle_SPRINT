import pygame

class PygameText():
    def __init__(
        self,
        screen : object,
        text : str,
        font : str | None,
        font_size : int,
        x : int,
        y : int):
        
        self.button_font = pygame.font.Font(font, font_size)
        self.button_text = self.button_font.render(text, True, (0, 0, 0))
        screen.blit(self.button_text, (x, y))