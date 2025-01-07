from ...tools.storage import storage
from ...widgets.pygame_button import PygameButton
from ...widgets.pygame_image import PygameImage

class AbilityButton():
    def __init__(self, ability, coordinates, size, event, type):
        self.ability = ability
        self.coordinates = coordinates
        self.size = size
        self.type = type

        if self.type == "buy":
            self.function = lambda: None
        elif self.type == "pick":
            self.function = lambda: storage.storage_dict["AbilityManager"].pick_ability(ability)

        self.button = PygameButton(
            path = ability.image_path,
            coordinates = coordinates,
            size = size,
            event = event,
            function = self.function
        )

        if self.type == "pick" and self.ability.name == storage.storage_dict["AbilityManager"].picked_ability:
            picked_image = PygameImage(
                path = "static/images/select.png",
                coordinates = coordinates,
                size = size
            )
