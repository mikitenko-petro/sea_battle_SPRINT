from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text import PygameText
from ..game_widgets.buy_ability_button import BuyAbilityButton
from .ability_button import AbilityButton
from ..tools.pygame_storage import pygame_storage

class AbilityShopLabel():
    def __init__(self, x, y, event):
        self.x = x
        self.y = y
        self.event = event

        self.ability_shop_label = PygameText(
            text = "Ability Shop",
            font = "static/fonts/alagard.ttf",
            font_size = 40,
            x = self.x + 100,
            y = self.y + 10,
        )

        for index, ability in enumerate(pygame_storage.storage_dict["AbilityManager"].ability_dict):
            ability_icon = AbilityButton(
                ability = pygame_storage.storage_dict["AbilityManager"].ability_dict[ability],
                coordinates = (self.x + 10, self.y + 60 + index*70),
                size = (50, 50),
                event = event,
                type = "buy"
            )

            ability_description = PygameText(
                text = pygame_storage.storage_dict["AbilityManager"].ability_dict[ability].description,
                font_size = 25,
                x = self.x + 70,
                y = self.y + 70 + index*70
            )

            buy_ability_button = BuyAbilityButton(
                coordinates = (self.x + 335, self.y + 60 + index*70),
                size = (50, 50),
                event = event,
                function = lambda: pygame_storage.storage_dict["AbilityManager"].ability_dict[ability].buy(),
                price = pygame_storage.storage_dict["AbilityManager"].ability_dict[ability].price,
            )