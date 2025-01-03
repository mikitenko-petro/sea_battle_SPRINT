from ...tools.pygame_storage import pygame_storage

class Ability():
    def __init__(self):
        self.title = None
        self.image_path = None
        self.amount = 0
        self.price = 0
    
    def buy(self):
        if pygame_storage.storage_dict["medals"] >= self.price:
            self.amount += 1