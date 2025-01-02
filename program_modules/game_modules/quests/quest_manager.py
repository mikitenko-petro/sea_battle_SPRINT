from ...tools.pygame_storage import pygame_storage
from .first_kill_quest import FirstKillQuest
from .first_kill_largest_ship_quest import FirstKillLargestShipQuest
from .kill_two_ships_in_time_quest import KillShipInTimeQuest
from .first_kill_all_smallest_ships_quest import FirstKillAllSmallestShipsQuest
from .in_first_move_hit_enemy_quest import HitShipInFirstMove

class QuestManager():
    def __init__(self):
        self.quests_list = [
            FirstKillQuest(),
            FirstKillLargestShipQuest(),
            KillShipInTimeQuest(),
            FirstKillAllSmallestShipsQuest(),
            HitShipInFirstMove(),
        ]

        pygame_storage.add_variable({"medals" : 0})

    def check_all_quests(self):
        for quest in self.quests_list:
            if quest.quest_complite:
                pygame_storage.storage_dict["medals"] += quest.medals
                quest.medals = 0

            quest.check_quest_done()
            