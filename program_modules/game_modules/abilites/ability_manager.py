from ...tools.pygame_storage import pygame_storage
from .artilery import Artilery
from .radio_set import RadioSet
from .shield import Shield

class AbilityManager():
    def __init__(self):
        self.ability_dict = {
            "Shield": Shield(),
            "RadioSet": RadioSet(),
            "Artilery": Artilery(),
        }

        self.picked_abilty = None

    def pick_ability(self, ability):
        if self.picked_abilty == None:
            self.picked_abilty = f"{ability.__class__.__name__}"
        else:
            self.picked_abilty = None