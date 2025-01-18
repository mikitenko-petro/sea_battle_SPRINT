from ...tools.storage import storage
from .parent_achievement_class import Achievement

class ThreeWinAchievement(Achievement):
    def __init__(self):
        Achievement.__init__(self)

        self.title = "Third win"
        self.description = "Make 3 victories"
        self.image_path = "static/images/third_win_icon.png"

    def check_complete(self):
        if storage.storage_dict["StatsManager"].stats_dict["winned_games"] >= 3:
            self.is_complete = True