from ...tools.pygame_storage import pygame_storage
from .parent_achievement_class import Achievement

class FirstWinAchievement(Achievement):
    def __init__(self):
        Achievement.__init__(self)

        self.title = "First win"
        self.description = "Congratulations, you've made your first victory!"
        self.image_path = "static/images/first_win_icon.png"

    def check_complete(self):
        if pygame_storage.storage_dict["winned_games"] > 0:
            self.is_complete = True