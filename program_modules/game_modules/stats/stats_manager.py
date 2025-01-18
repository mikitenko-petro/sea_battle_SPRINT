from ...tools.json_manager import read_json, write_json
import os

class StatsManager():
    def __init__(self):
        self.stats_dict = {
            "winned_games" : 0,
            "destroed_4x1_ships" : 0,
        }

        self.stats_data = {}

    def load_stats(self):
        try:
            self.stats_dict = read_json("static/json/stats.json")
            print(self.stats_data)
        except FileNotFoundError:
            pass

    def save_stats(self):
        if not os.path.exists("static/json/stats.json"):
            write_json("static/json/stats.json", self.stats_dict)

        if self.stats_data != self.stats_dict:
            self.stats_data = self.stats_dict.copy()
            write_json("static/json/stats.json", self.stats_data)