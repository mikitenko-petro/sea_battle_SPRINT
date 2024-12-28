import pygame
from ..widgets.pygame_text import PygameText
from ..tools.pygame_storage import pygame_storage

class FpsCounter(PygameText):
    def __init__(self, screen, x, y):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.x = x
        self.y = y
        pygame_storage.add_variable({"FPS": 0})

    def render(self):
        pygame_storage.storage_dict["FPS"] = round(self.clock.get_fps())

        text = PygameText(
            screen = self.screen,
            text = str(pygame_storage.storage_dict["FPS"]),
            font_size = 20,
            x = self.x,
            y = self.y
        )