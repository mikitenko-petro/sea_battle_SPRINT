from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_hitbox import PygameHitBox
from ..tools.storage import storage

class CapitanIcon(PygameHitBox):
    def __init__(self, color, coordinates, size, emotion):
        PygameHitBox.__init__(self, coordinates, size)
        self.color = color
        self.status = emotion
        self.path = "static/images/Base_capitan.png"
        

        match self.status:
            case "base":
                self.path = "static/images/Base_capitan.png"

            case "angry":
                self.path = "static/images/angry_capitan.png"

            case "strange":
                self.path = "static/images/strange_capitan.png"

            case "scared":
                self.path = "static/images/scared_capitan.png"

        capitan_image = PygameImage(
            path = self.path,
            coordinates = (self.x, self.y),
            size = (self.width, self.height)
        )

