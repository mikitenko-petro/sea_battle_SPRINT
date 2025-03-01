from ...tools.storage import storage
from .parent_quest_class import Quest

class FirstKillAllSmallestShipsQuest(Quest):
    def __init__(self):
        Quest.__init__(self)
        
        self.title = "destroy all 1x1 ships first"
        self.image_path = "static/images/kill_4_ships_icon.png"
        self.medals = 2
    
    def check_quest_done(self):
        ships1x1defeated = 0
        for dummy_ship in storage.storage_dict["dummy_ship_list"]:
            if dummy_ship.type == "1x1":
                ships1x1defeated += 1

        our1x1shipsdefeated = 0
        for ship in storage.storage_dict["ship_list"]:
            if ship.type == "1x1" and ship.status == "defeated":
                our1x1shipsdefeated += 1
        
        if our1x1shipsdefeated < 4 and ships1x1defeated == 4:
            self.give_medals()
            self.quest_complite = True