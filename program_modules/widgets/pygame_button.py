import pygame
from .pygame_image import PygameImage

class PygameButton():
    def __init__(self, screen, path, coordinates, size, event, font_size):
        self.button_image = PygameImage(screen, path, coordinates, size)
        self.button_x, self.button_y = coordinates
        self.button_width, self.button_height = size
        self.button_font = pygame.font.Font(None, font_size)
        self.button_text = self.button_font.render("Start", True, (0, 0, 0))
        self.screen_size = screen.get_size()
        self.screen_width, self.screen_height = self.screen_size
        text_procent = 10/3.53
        text_procent_varable = (text_procent*font_size)/3.53
        text_x = self.button_x  - text_procent_varable + (self.button_width/2)
        text_y = self.button_y + self.button_height/2.5
        screen.blit(self.button_text, (text_x, text_y))

        self.click_checking(event)

    def click_checking(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for pygame_event in event: 
            if mouse_x >= self.button_x and mouse_x <= self.button_x + self.button_width:
                if mouse_y >= self.button_y and mouse_y <= self.button_y + self.button_height:
                    if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                        print(2232)