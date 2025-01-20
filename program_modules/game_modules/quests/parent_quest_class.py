from ...tools.storage import storage
from ...widgets.temporary_object import TemporaryObject
from ...widgets.pygame_image import PygameImage
from ...widgets.pygame_text import PygameText

class Quest():
    def __init__(self):
        self.quest_complite = False
        self.title = None
        self.image_path = None
        self.medals = 0

    def give_medals(self):
        if not self.quest_complite:
            storage.storage_dict["medals"] += self.medals

            storage.storage_dict["temporary_objects"].append(
                TemporaryObject(
                    miliseconds = 3000,
                    object_list = [
                        PygameText(
                            text = "+",
                            x = 60,
                            y = 10,
                            font_size = 50,
                        ),
                        PygameImage(
                            path = "static/images/medal.png",
                            coordinates = (70, 10),
                            size = (50, 50),
                        ),
                        PygameText(
                            text = str(self.medals),
                            x = 120,
                            y = 10,
                            font_size = 50,
                        ),
                    ]
                )
            )