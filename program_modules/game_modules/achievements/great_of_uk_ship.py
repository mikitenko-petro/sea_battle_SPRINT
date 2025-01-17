from ...tools.storage import storage
from .parent_achievement_class import Achievement
from .unlock_class import Unlock

class GreatOfUKship(Achievement):
    def __init__(self):
        Achievement.__init__(self)

        self.title = "Sink the pride of the British Navy"
        self.description = "Sink 4x1 ship 5 times"
        self.image_path = "static/images/first_win_icon.png"

    def check_complete(self):
        for ship in storage.storage_dict["ship_list"]:
            if ship.type == "4x1" and ship.status == "defeated":
                storage.storage_dict["destroed_4x1_ships"] += 1
        if storage.storage_dict["destroed_4x1_ships"] >= 5:    
            self.is_complete = True