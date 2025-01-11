from ...tools.storage import storage
from .parent_achievement_class import Achievement
from .unlock_class import Unlock

class ThreeWinAchievement(Achievement):
    def __init__(self):
        Achievement.__init__(self)

        self.title = "Third win"
        self.description = "Make 3 victories"
        self.image_path = "static/images/third_win_icon.png"
        
        self.unlock = Unlock(
            path = "static/images/rocket_artilery.png",
            ability = "RocketArtilery"
        )

    def check_complete(self):
        if storage.storage_dict["StatsManager"].stats_dict["winned_games"] >= 3:
            self.is_complete = True