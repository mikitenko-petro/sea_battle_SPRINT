from .pygame_image import PygameImage
from .pygame_text import PygameText

class PygameLabel(PygameImage, PygameText):
    def __init__(
        self,
        screen : object,
        path : str,
        coordinates : tuple,
        size : tuple,
        text : str,
        font : str | None,
        font_size : int):

        x, y = coordinates
        width, height = size

        PygameImage.__init__(self, screen, path, coordinates, size)

        text_x = x + width/2 - len(text)*font_size/6
        text_y = y + height/2 - font_size/4

        PygameText.__init__(self, screen, text, font, font_size, text_x, text_y)

