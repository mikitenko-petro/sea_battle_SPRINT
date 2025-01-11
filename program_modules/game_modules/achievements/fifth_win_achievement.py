from ...tools.storage import storage
from .parent_achievement_class import Achievement
from .unlock_class import Unlock

class FifthWinAchievement(Achievement):
    def __init__(self):
        Achievement.__init__(self)

        self.title = "Fifth win"
        self.description = "Make your fifth victory!"
        self.image_path = "static/images/fifth_win_icon.png"
        
        self.unlock = Unlock(
            path = "static/images/radio_set.png",
            ability = "RadioSet",
        )

    def check_complete(self):
        if storage.storage_dict["StatsManager"].stats_dict["winned_games"] >= 5:
            self.is_complete = True