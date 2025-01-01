from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text import PygameText
from ..widgets.pygame_button import PygameButton
from ..tools.pygame_storage import pygame_storage

class QuestLabel():
    def __init__(self, x, y, event):
        self.x = x
        self.y = y
        self.show = False

        self.show_button = PygameButton(
            coordinates = (0, 0),
            size = (50, 50),
            event = event,
            function = self.show_quests,
            path = "",
        )

        if self.show:
            #setup
            self.bg = PygameImage(
                path = "static/images/grey_label.png",
                coordinates = (x, y),
                size = (200, 700),
            )

            self.title = PygameText(
                text = "Quests",
                font_size = 40,
                x = x + 10,
                y = y + 10,
                font = "static/fonts/alagard.ttf",
            )

            #first fire quest

            self.first_fire_quest_icon = PygameImage(
                path = "static/images/first_hit.png",
                coordinates = (x + 10, y + 70),
                size = (50, 50),
            )

            self.first_fire_quest_title = PygameText(
                text = "destroy the ship first",
                font_size = 20,
                x = x + 70,
                y = y + 70,
            )
        
    def show_quests(self):
        self.show = not self.show