from ...tools.storage import storage
from .parent_quest_class import Quest

class HitShipInFirstMove(Quest):
    def __init__(self):
        Quest.__init__(self)

        self.title = "hit the ship at start"
        self.image_path = "static/images/hit_at_begin_icon.png"
        self.medals = 2
    
    def check_quest_done(self):
        if storage.storage_dict["moves"] == 1:
            if storage.storage_dict["hits"] >= 1:
                self.give_medals()
                self.quest_complite = True