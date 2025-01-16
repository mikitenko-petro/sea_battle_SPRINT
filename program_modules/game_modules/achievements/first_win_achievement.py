from ...tools.storage import storage
from .parent_achievement_class import Achievement
from .unlock_class import Unlock

class FirstWinAchievement(Achievement):
    def __init__(self):
        Achievement.__init__(self)

        self.title = "First win"
        self.description = "Make your first victory!"
        self.image_path = "static/images/first_win_icon.png"
        
        self.unlock = Unlock(
            path = "static/images/shield.png",
            ability = "Shield"
        )

    def check_complete(self):
        if storage.storage_dict["StatsManager"].stats_dict["winned_games"] > 0:
            self.is_complete = True