from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_text import PygameText
from ..tools.storage import storage
from ..game_widgets.achievement_label import AchievementLabel

#Робимо клас для Основної сцени гри
class AchievementScreenScene():
    #Робимо функцію ініт для задання параметрів та основних модулів
    def __init__(self):
        pass

    #Робим метод для початкогово екрану
    def run(self, event : object):
        #Робим фон для початкової сцени
        background_image = PygameImage(
            path = "static/images/achievements_scene_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )

        return_button = PygameButton(
            coordinates = (0, 0),
            size = (50, 50),
            event = event,
            path = "static/images/apply_button.png",
            function = lambda: storage.storage_dict["SceneManager"].change_scene(scene = "main")
        )

        title = PygameText(
            text = "Achievements",
            font_size = 120,
            x = 240,
            y = 550,
            font = "static/fonts/alagard.ttf",
            color = (255, 255, 0)
        )

        achievement_label = AchievementLabel()