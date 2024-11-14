import pygame

class PygameText():
    def __init__(self, screen, text, x, y):
        self.button_font = pygame.font.Font(None, 20)
        self.button_text = self.button_font.render(text, True, (0, 0, 0))
        screen.blit(self.button_text, (x, y))