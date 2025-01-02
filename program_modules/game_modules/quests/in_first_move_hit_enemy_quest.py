from ...tools.pygame_storage import pygame_storage
from .parent_quest_class import Quest

class HitShipInFirstMove(Quest):
    def __init__(self):
        Quest.__init__(self)

        self.title = "hit the ship at start"
        self.image_path = "static/images/first_kill_icon.png"
        self.medals = 5
    
    def check_quest_done(self):
        if pygame_storage.storage_dict["moves"] == 1:
            if pygame_storage.storage_dict["hits"] >= 1:
                self.change_complite()