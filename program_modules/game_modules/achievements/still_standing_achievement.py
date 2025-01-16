from ...tools.storage import storage
from .parent_achievement_class import Achievement
from .unlock_class import Unlock

class FirstWinAchievement(Achievement):
    def __init__(self):
        Achievement.__init__(self)

        self.title = "I am still standing"
        self.description = "Make victory with one 1x1 ship!"
        self.image_path = "static/images/first_win_icon.png"

    def check_complete(self):
        defeated_ships = 0
        for ship in storage.storage_dict["ship_list"]:
            if ship.type == "1x1" and ship.status == "defeated":
                defeated_ships += 1
        if defeated_ships == 3 and storage.storage_dict["StatsManager"].stats_dict["winned_games"] > 0:    
            self.is_complete = True