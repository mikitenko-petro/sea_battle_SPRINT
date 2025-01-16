from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text import PygameText
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_rect import PygameRect
from ..widgets.pygame_check_box import PygameCheckBox
from ..tools.storage import storage
from ..game_modules.quests.quest_manager import QuestManager
from .ability.ability_shop_label import AbilityShopLabel

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

        storage.add_variable({"QuestManager": QuestManager()})

        if storage.storage_dict["show_quests"]:  
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
                text = storage.storage_dict["medals"],
                font_size = 40,
                x = self.x + 320,
                y = self.y + 20,
            )

            medal_image = PygameImage(
                path = "static/images/medal.png",
                coordinates = (self.x + 350, self.y + 10),
                size = (50, 50)
            )

            self.quit_button = PygameButton(
                coordinates = (50, 0),
                size = (750, 700),
                event = event,
                function = self.show_quests
            )

            for index, quest in enumerate(storage.storage_dict["QuestManager"].quests_list):
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

            ability_shop_label = AbilityShopLabel(
                x = self.x + 10,
                y = self.y + 150 + index*70,
                event = event
            )
            
        storage.storage_dict["QuestManager"].check_all_quests()

    def show_quests(self):
        storage.storage_dict["show_quests"] = not storage.storage_dict["show_quests"]