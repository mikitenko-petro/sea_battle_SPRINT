from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_rect import PygameRect
from ..widgets.pygame_hitbox import PygameHitBox
from ..widgets.pygame_text import PygameText
from ..tools.pygame_storage import pygame_storage

class BuyAbilityButton(PygameButton, PygameHitBox):
    def __init__(
            self,
            coordinates : tuple,
            size : tuple,
            event : object,
            price : int,
            function : object):
        
        PygameButton.__init__(
            self,
            coordinates = coordinates,
            size = size,
            event = event,
            function = function
        )

        PygameHitBox.__init__(
            self,
            coordinates = coordinates,
            size = size
        )

        if pygame_storage.storage_dict["medals"] < price:
            self.rect = PygameRect(
                coordinates = coordinates,
                size = size,
                color = (100, 100, 100),
            )   
        else:
            self.rect = PygameRect(
                coordinates = coordinates,
                size = size,
                color = (0, 255, 0)
            )

        self.rect.draw(border = 0)

        self.medal = PygameImage(
            coordinates = (self.x + 20, self.y + 15),
            size = (32, 32),
            path = "static/images/medal.png",
        )

        self.price_text = PygameText(
            text = price,
            font_size = 40,
            x = self.x + 5,
            y = self.y + 15,
        )

        self.border = PygameImage(
            coordinates = (self.x, self.y),
            size = (self.width, self.height),
            path = "static/images/cell.png",
        )