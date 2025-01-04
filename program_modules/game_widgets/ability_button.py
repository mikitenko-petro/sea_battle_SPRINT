from ..tools.pygame_storage import pygame_storage
from ..widgets.pygame_button import PygameButton

class AbilityButton():
    def __init__(self, ability, coordinates, size, event, type):
        self.ability = ability
        self.coordinates = coordinates
        self.size = size
        self.type = type

        if self.type == "buy":
            self.function = lambda: None
        elif self.type == "pick":
            self.function = lambda: pygame_storage.storage_dict["AbilityManager"].pick_ability(self)

        self.button = PygameButton(
            path = pygame_storage.storage_dict["AbilityManager"].ability_dict[ability.__class__.__name__].image_path,
            coordinates = coordinates,
            size = size,
            event = event,
            function = self.function
        )