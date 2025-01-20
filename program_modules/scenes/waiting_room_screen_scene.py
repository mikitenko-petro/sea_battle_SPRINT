from ..tools.storage import storage
from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text import PygameText

class WaitingRoomScreenScene():
    def __init__(self):
        ...

    def run(self, event):
        background_image = PygameImage(
            path = "static/images/sea_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )

        title_text = PygameText(
            text = "waiting for opponent",
            font = "static/fonts/alagard.ttf",
            font_size = 200,
            x = 100,
            y = 500,
        )