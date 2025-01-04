from .parent_ability_class import Ability

class Artilery(Ability):
    def __init__(self):
        Ability.__init__(self)
        
        self.title = "Artilery"
        self.image_path = "static/images/rocket_artilery.png"
        self.description = "Land 3 shots on 3x3 area"

        self.amount = 0
        self.price = 3