from ...tools.pygame_storage import pygame_storage
from .parent_quest_class import Quest

class FirstKillQuest(Quest):
    def __init__(self):
        Quest.__init__(self)
        
        self.title = "destroy the ship first"
        self.image_path = "static/images/first_kill_icon.png"
        self.medals = 1
    
    def check_quest_done(self):
        if len(pygame_storage.storage_dict["dummy_ship_list"]) == 1:
            is_defeated = False
            for ship in pygame_storage.storage_dict["ship_list"]:
                if ship.status == "defeated":
                    is_defeated = True
            
            if not is_defeated:
                self.change_complite()