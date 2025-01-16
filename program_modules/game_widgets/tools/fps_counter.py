from ...widgets.pygame_text import PygameText
from ...tools.storage import storage

class FpsCounter(PygameText):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        storage.add_variable({"FPS": 0})

    def render(self):
        storage.storage_dict["FPS"] = round(storage.storage_dict["clock"].get_fps())

        text = PygameText(
            text = str(storage.storage_dict["FPS"]),
            font_size = 20,
            x = self.x,
            y = self.y
        )