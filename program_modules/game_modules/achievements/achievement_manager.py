from ...tools.json_manager import read_json, write_json
from .first_win_achievement import FirstWinAchievement
from .three_win_achievement import ThreeWinAchievement
from .fifth_win_achievement import FifthWinAchievement
from .still_standing_achievement import StillStanding
from ...tools.storage import storage
import os

class AchievementManager():
    def __init__(self):
        self.achievements_dict = {
            "FirstWinAchievement": FirstWinAchievement(),
            "ThreeWinAchievement": ThreeWinAchievement(),
            "FifthWinAchievement": FifthWinAchievement(),
            "StillStanding": StillStanding(),
            
        }

        self.achievements_data = {}
        for achievement in self.achievements_dict.values():
            self.achievements_data.update(
                {
                    f"{achievement.__class__.__name__}": {
                        "complete_count": achievement.complete_count,
                        "is_complete": achievement.is_complete
                        }
                }
            )
            
    def load_achievements(self):
        try:
            self.achievements_data = read_json("static/json/achievements.json")
        except FileNotFoundError:
            pass

        for achievement_name in self.achievements_data:
            self.achievements_dict[achievement_name].complete_count = self.achievements_data[achievement_name]["complete_count"]
            self.achievements_dict[achievement_name].is_complete = self.achievements_data[achievement_name]["is_complete"]

    def save_achievements(self):
        if not os.path.exists("static/json/achievements.json"):
            write_json("static/json/achievements.json", self.achievements_data)

        for name in self.achievements_dict:
            if name in self.achievements_data:
                if self.achievements_dict[name].is_complete:
                    self.achievements_data[name]["is_complete"] = True
                    write_json("static/json/achievements.json", self.achievements_data)

                elif self.achievements_dict[name].complete_count != self.achievements_data[name]["complete_count"]:
                    self.achievements_data[name]["complete_count"] = self.achievements_dict[name].complete_count
                    write_json("static/json/achievements.json", self.achievements_data)

    def check_all_achievements(self):
        for achievement in self.achievements_dict:
            self.achievements_dict[achievement].check_complete()

        self.save_achievements()