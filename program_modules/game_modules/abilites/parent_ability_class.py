from ...tools.pygame_storage import pygame_storage

class Ability():
    def __init__(self):
        self.title = None
        self.image_path = None
        self.description = None
        self.name = self.__class__.__name__
        self.amount = 0
        self.price = 0
    
    def buy(self):
        if pygame_storage.storage_dict["medals"] >= self.price:
            self.amount += 1
            pygame_storage.storage_dict["medals"] -= self.price

    def usage(func):
        def handle(self):
            if self.amount > 0:
                func(self)

                self.amount -= 1
                pygame_storage.storage_dict["player_turn"] = False
                pygame_storage.storage_dict["AbilityManager"].picked_ability = None

        return handle