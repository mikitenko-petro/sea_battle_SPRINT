from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text import PygameText
from ..widgets.pygame_check_box import PygameCheckBox
from ..tools.storage import storage

class AchievementLabel():
    def __init__(self):
        for index, achievement_name in enumerate(storage.storage_dict["AchievementManager"].achievements_dict):
            initial_x = 60
            initial_y = 60

            delta_y = 150

            achievement_bg = PygameImage(
                path = "static/images/blue_label.png",
                coordinates = (initial_x + 15, initial_y + 15 + index*delta_y),
                size = (128*4, 32*4)
            )

            achievement_image = PygameImage(
                path = storage.storage_dict["AchievementManager"].achievements_dict[achievement_name].image_path,
                coordinates = (initial_x + 25, initial_y + 25 + index*delta_y),
                size = (50, 50)
            )
            
            achievement_title = PygameText(
                text = storage.storage_dict["AchievementManager"].achievements_dict[achievement_name].title,
                font_size = 40,
                x = initial_x + 85, 
                y = initial_y + 25 + index*delta_y
            )

            achievement_description = PygameText(
                text = storage.storage_dict["AchievementManager"].achievements_dict[achievement_name].description,
                font_size = 25,
                x = initial_x + 25,
                y = initial_y + 85 + index*delta_y
            )

            unlock_image = PygameImage(
                path = storage.storage_dict["AchievementManager"].achievements_dict[achievement_name].unlock.path,
                coordinates = (initial_x + 405, initial_y + 25 + index*delta_y),
                size = (50, 50)
            )
            
            achievement_check_box = PygameCheckBox(
                coordinates = (initial_x + 460, initial_y + 25 + index*delta_y),
                size = (50, 50)
            )

            achievement_check_box.complete = storage.storage_dict["AchievementManager"].achievements_dict[achievement_name].is_complete
            achievement_check_box.draw()