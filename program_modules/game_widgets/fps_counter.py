from ..widgets.pygame_text import PygameText
from ..tools.pygame_storage import pygame_storage

class FpsCounter(PygameText):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame_storage.add_variable({"FPS": 0})

    def render(self):
        pygame_storage.storage_dict["FPS"] = round(pygame_storage.storage_dict["clock"].get_fps())

        text = PygameText(
            text = str(pygame_storage.storage_dict["FPS"]),
            font_size = 20,
            x = self.x,
            y = self.y
        )