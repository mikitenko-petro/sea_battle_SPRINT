from .parent_ability_class import Ability

class Shield(Ability):
    def __init__(self):
        Ability.__init__(self)
        
        self.title = "Shield"
        self.image_path = "static/images/shield.png"
        self.description = "Protect one tile of ship"

        self.amount = 0
        self.price = 3