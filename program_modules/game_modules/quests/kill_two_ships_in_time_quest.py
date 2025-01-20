from ...tools.storage import storage
from .parent_quest_class import Quest

class KillShipInTimeQuest(Quest):
    def __init__(self):
        Quest.__init__(self)

        self.title = "destroy 2 ships in 10 moves"
        self.image_path = "static/images/fast_attack_icon.png"
        self.medals = 3
    
    def check_quest_done(self):
        if storage.storage_dict["moves"] <= 10:
            if len(storage.storage_dict["dummy_ship_list"]) >= 2:
                self.give_medals()
                self.quest_complite = True