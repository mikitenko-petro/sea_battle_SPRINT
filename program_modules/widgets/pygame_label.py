from .pygame_image import PygameImage
from .pygame_text import PygameText
#Робим клас для тексту
class PygameLabel(PygameImage, PygameText):
    def __init__(
        self,
        path : str,
        coordinates : tuple,
        size : tuple,
        text : str,
        font : str | None = None,
        font_size : int = 20):

        #Робим розміри та розположення тексту
        x, y = coordinates
        width, height = size

        PygameImage.__init__(
            self, path, coordinates, size)

        #Розположення тексту
        text_x = x + width/2 - len(text)*font_size/6
        text_y = y + height/2 - font_size/4

        PygameText.__init__(
            self,
            text = text,
            font_size = font_size,
            x = text_x,
            y = text_y,
            font = font
        )