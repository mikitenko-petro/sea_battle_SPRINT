from .parent_ability_class import Ability

class RadioSet(Ability):
    def __init__(self):
        Ability.__init__(self)
        
        self.title = "Radio Set"
        self.image_path = "static/images/radio_set.png"
        self.description = "Scan 3x3 area for ships"

        self.amount = 0
        self.price = 5