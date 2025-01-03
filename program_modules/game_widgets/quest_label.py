from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text import PygameText
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_rect import PygameRect
from ..widgets.pygame_check_box import PygameCheckBox
from ..tools.pygame_storage import pygame_storage
from ..game_modules.quests.quest_manager import QuestManager
from ..game_modules.abilites.parent_ability_class import Ability

class QuestLabel():
    def __init__(self, x, y, event):
        self.x = x
        self.y = y

        self.show_button = PygameButton(
            coordinates = (0, 0),
            size = (50, 50),
            event = event,
            function = self.show_quests,
            path = "static/images/quest_icon.png",
        )

        self.abilites_list = ["Radar", "Drone", "Shield"]

        pygame_storage.add_variable({"QuestManager": QuestManager()})

        if pygame_storage.storage_dict["show_quests"]:
            self.bg = PygameRect(
                coordinates = (x, y),
                size = (400, 700),
                color = (48, 96, 130),
            )
            self.bg.draw(0)

            self.title = PygameText(
                text = "Quests",
                font_size = 40,
                x = x + 120,
                y = y + 10,
                font = "static/fonts/alagard.ttf",
            )

            medal_text = PygameText(
                text = pygame_storage.storage_dict["medals"],
                font_size = 40,
                x = self.x + 320,
                y = self.y + 20,
            )

            medal_image = PygameImage(
                path = "static/images/medal.png",
                coordinates = (self.x + 350, self.y + 10),
                size = (50, 50)
            )

            for index, quest in enumerate(pygame_storage.storage_dict["QuestManager"].quests_list):
                quest_image = PygameImage(
                    path = quest.image_path,
                    coordinates = (self.x + 10, self.y + 60 + index*70),
                    size = (50, 50)
                )
                
                quest_title = PygameText(
                    text = quest.title,
                    font_size = 30,
                    x = self.x + 70, 
                    y = self.y + 70 + index*70
                )
                
                quest_check_box = PygameCheckBox(
                    coordinates = (self.x + 350, self.y + 65 + index*70),
                    size = (40, 40)
                )

                medal_icon = PygameImage(
                    path = "static/images/medal.png",
                    coordinates = (self.x + 65, self.y + 90 + index*70),
                    size = (25, 25)
                )

                medal_count_text = PygameText(
                    text = quest.medals,
                    font_size = 25,
                    x = self.x + 90,
                    y = self.y + 90 + index*70
                )

                quest_check_box.complete = quest.quest_complite
                quest_check_box.draw()
            
            for index, ability in enumerate(self.abilites_list):

                ability_title = PygameText(
                    text = ability,
                    font_size = 25,
                    x = self.x + 10,
                    y = self.y + 500 + index*70
                )
                buy_ability_button = PygameButton(
                    coordinates = (self.x + 300, self.y + 500 + index*70),
                    size = (100, 40),
                    event = event,
                    function = lambda: print("Buy"),
                    text = "Buy"
                )


        pygame_storage.storage_dict["QuestManager"].check_all_quests()
                

    def show_quests(self):
        pygame_storage.storage_dict["show_quests"] = not pygame_storage.storage_dict["show_quests"]