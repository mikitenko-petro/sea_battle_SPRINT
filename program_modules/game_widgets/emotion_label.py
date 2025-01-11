from .capitan_icon import CapitanIcon
from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..tools.storage import storage

class EmotionLable():
    def __init__(self, event):
        self.x = 0
        self.y = 0
        storage.add_variable({"show_emotion_label": False})

        emotion_button = PygameButton(
            coordinates = (0, 65),
            size = (50, 50),
            event = event,
            function = self.show_emotion_label
        )

        if storage.storage_dict["show_emotion_label"]:
            panel = PygameImage(
                path = "static/images/blue_label.png",
                coordinates = (465, 85),
                size = (128*2, 32*2)
            )

            index = 0
            
            for emotion in ["angry", "strange", "scared", "base"]:
                emotion_icon = CapitanIcon(
                    color = "blue",
                    coordinates = (475 + 60*index, 90),
                    size = (50, 50),
                    emotion = emotion
                )

                index += 1
    
    def show_emotion_label(self):
        storage.storage_dict["show_emotion_label"] = not storage.storage_dict["show_emotion_label"]