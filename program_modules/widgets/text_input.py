import pygame
from .pygame_button import PygameButton
from .pygame_image import PygameImage
from .pygame_text import PygameText
from ..search_path import search_path

class TextInput():
    def __init__(self, size, coordinates, event, screen):
        x, y = coordinates
        self.input_image = PygameImage(screen = screen, coordinates = coordinates, size = size, path = "static/images/input_field.png")
        self.input_text = PygameText(screen = screen, text = "Enter ip adress", font = None,font_size = 20, x = x, y = y)
        




