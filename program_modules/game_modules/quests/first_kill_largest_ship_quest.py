from ...tools.pygame_storage import pygame_storage
from .parent_quest_class import Quest

class FirstKillLargestShipQuest(Quest):
    def __init__(self):
        Quest.__init__(self)
        
        self.title = "destroy the 4x1 ship first"
        self.image_path = "static/images/first_kill_icon.png"
        self.medals = 3
    
    def check_quest_done(self):
        ship4x1defeated = False
        for dummy_ship in pygame_storage.storage_dict["dummy_ship_list"]:
            if dummy_ship.type == "4x1":
                ship4x1defeated = True

        for ship in pygame_storage.storage_dict["ship_list"]:
            if ship.type == "4x1" and ship.status != "defeated" and ship4x1defeated:
                self.quest_complite = True