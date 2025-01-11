from .pygame_image import PygameImage
from .pygame_button import PygameButton
from .pygame_hitbox import PygameHitBox

class PygameCheckBox(PygameHitBox):
    def __init__(self, coordinates, size, clickable : bool = False):
        PygameHitBox.__init__(self, coordinates, size)

        self.complete = False

        if clickable:
            self.check_box = PygameButton(
                coordinates = coordinates,
                size = size,
                path = "static/images/cell.png",
                function = self.change_status
            )

        else:
            self.check_box = PygameImage(
                coordinates = coordinates,
                size = size,
                path = "static/images/cell.png"
            )
    
    def change_status(self):
        self.complete = not self.complete

    def draw(self):
        if self.complete:
            self.complete_image = PygameImage(
                path = "static/images/complete.png",
                coordinates = (self.x, self.y),
                size = (self.width, self.height)
            )