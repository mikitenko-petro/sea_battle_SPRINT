from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text import PygameText
from ..widgets.pygame_button import PygameButton
from ..widgets.pygame_rect import PygameRect
from ..widgets.pygame_check_box import PygameCheckBox
from ..tools.pygame_storage import pygame_storage

class AchievementLabel():
    def __init__(self, x, y, event):
        self.x = x
        self.y = y

        for index, achievement_name in enumerate(pygame_storage.storage_dict["AchievementManager"].achievements_dict):
            achievement_image = PygameImage(
                path = pygame_storage.storage_dict["AchievementManager"].achievements_dict[achievement_name].image_path,
                coordinates = (self.x + 10, self.y + 60 + index*70),
                size = (50, 50)
            )
            
            achievement_title = PygameText(
                text = pygame_storage.storage_dict["AchievementManager"].achievements_dict[achievement_name].title,
                font_size = 30,
                x = self.x + 70, 
                y = self.y + 70 + index*70
            )
            
            achievement_check_box = PygameCheckBox(
                coordinates = (self.x + 350, self.y + 65 + index*70),
                size = (40, 40)
            )

            achievement_check_box.complete = pygame_storage.storage_dict["AchievementManager"].achievements_dict[achievement_name].is_complete
            achievement_check_box.draw()