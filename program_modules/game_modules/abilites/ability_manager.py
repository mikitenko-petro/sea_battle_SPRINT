from .artilery import Artilery
from .radio_set import RadioSet
from .shield import Shield

class AbilityManager():
    def __init__(self):
        self.ability_dict = {
            "Shield": Shield(),
            "Artilery": Artilery(),
            "RadioSet": RadioSet(),
        }

        self.picked_ability = None

    def pick_ability(self, ability):
        if (self.picked_ability == None or self.picked_ability != f"{ability.__class__.__name__}") and ability.amount > 0:
            self.picked_ability = f"{ability.__class__.__name__}"

        else:
            self.picked_ability = None

        print(self.picked_ability)