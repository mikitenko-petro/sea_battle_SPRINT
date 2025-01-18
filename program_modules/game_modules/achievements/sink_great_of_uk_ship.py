from ...tools.storage import storage
from .parent_achievement_class import Achievement

class SinkGreatOfUKship(Achievement):
    def __init__(self):
        Achievement.__init__(self)

        self.open_check = False

        self.title = "Pride and Extreme Prejudice"
        self.description = "Sink 4x1 ship 5 times"
        self.image_path = "static/images/first_win_icon.png"

    def check_complete(self):
        if storage.storage_dict["StatsManager"].stats_dict["destroed_4x1_ships"] > 4:    
            self.is_complete = True