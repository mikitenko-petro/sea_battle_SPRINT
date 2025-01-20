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
        font_size : int = 20,
        color: tuple = (0, 0 ,0)):

        #Робим розміри та розположення тексту
        x, y = coordinates
        width, height = size

        label_image = PygameImage(path, coordinates, size)

        #Розположення тексту
        text_x = x + width/2 - len(text)*font_size/6
        text_y = y + height/2 - font_size/4

        label_text = PygameText(
            text = text,
            font_size = font_size,
            x = text_x,
            y = text_y,
            font = font,
            color = color,
        )