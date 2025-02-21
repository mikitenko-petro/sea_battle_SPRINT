from ...tools.storage import storage
from .parent_achievement_class import Achievement

class StillStanding(Achievement):
    def __init__(self):
        Achievement.__init__(self)

        if not self.is_complete:
            self.title = "I am still standing"
            self.description = "???"
            self.image_path = "static/images/secret_achievement_icon.png"
        else:
            self.title = "I am still standing"
            self.description = "win with one 1x1 ship"
            self.image_path = "static/images/i_am_still_standing_icon_achivement.png"

    def check_complete(self):
        if storage.storage_dict["SceneManager"].current_scene == "end":
            defeated_1x1_ships = 0
            defeated_ships = 0
            for ship in storage.storage_dict["ship_list"]:
                if ship.status == "defeated":
                    defeated_ships += 1
                if ship.type == "1x1" and ship.status == "defeated":
                    defeated_1x1_ships += 1
            if defeated_1x1_ships == 3 and defeated_ships == 9 and storage.storage_dict["StatsManager"].stats_dict["winned_games"] > 0:    
                self.is_complete = True