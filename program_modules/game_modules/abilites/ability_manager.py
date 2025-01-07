from ...tools.storage import storage
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

        self.picked_ability = None

    def pick_ability(self, ability):
        if self.picked_ability == None:
            self.picked_ability = f"{ability.__class__.__name__}"
        else:
            self.picked_ability = None

        print(self.picked_ability)