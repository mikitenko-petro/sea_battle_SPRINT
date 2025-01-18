from ...widgets.pygame_image import PygameImage
from ...widgets.pygame_text import PygameText
from ...widgets.pygame_hitbox import PygameHitBox
from .ability_button import AbilityButton
from ...tools.storage import storage

class AbilityLabel(PygameHitBox):
    def __init__(self, coordinates, event):
        PygameHitBox.__init__(self, coordinates, (300, 75))

        delta_x = 110

        self.bg = PygameImage(
            path = "static/images/blue_label.png",
            coordinates = coordinates,
            size = (self.width, self.height)
        )
            
        for index, ability in enumerate(storage.storage_dict["AbilityManager"].ability_dict):
            ability_button = AbilityButton(
                ability = storage.storage_dict["AbilityManager"].ability_dict[ability],
                coordinates = (self.x  + delta_x*index + 10, self.y + 10),
                size = (50, 50),
                event = event,
                type = "pick"
            )
            
            amount_text = PygameText(
                text = storage.storage_dict["AbilityManager"].ability_dict[ability].amount,
                font_size = 20,
                x = self.x + delta_x*index + 55,
                y = self.y + 60
            )