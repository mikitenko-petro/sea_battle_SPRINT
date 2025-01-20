from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_label import PygameLabel
from ..game_widgets.decorations.fire_animation_widget import FireAnimationWidget
from ..game_widgets.decorations.shield_widget import ShieldWidget
from ..tools.storage import storage
from ..game_modules.battle.ship_manager import ShipManager
from ..game_widgets.quest_label import QuestLabel
from ..game_widgets.ability.ability_label import AbilityLabel
from ..game_widgets.decorations.radio_set_animation import RadioSetAnimation

#Робим клас для ігрвого вікна
class GameScreneScene():
    #Робим метод ініт для задання пареммрів та модулів
    def __init__(self):
        storage.add_variable({"ENEMY_GRID" : None})
        storage.add_variable({"show_quests": False})
        storage.add_variable({"radio_animation": RadioSetAnimation()})

    #Робим метод для створення екрану гри
    def run(self, event : object):
        storage.storage_dict["collision_list"] = []
        
        #Робим фон
        background_image = PygameImage(
            path = "static/images/sea_bg.png",
            coordinates = (0, 0),
            size = (1200, 700)
        )

        storage.storage_dict["PLAYER_GRID"].show_grid(event)
        storage.storage_dict["PLAYER_GRID"].x = 50
        storage.storage_dict["PLAYER_GRID"].y = 180

        storage.storage_dict["ENEMY_GRID"].show_grid(event)

        ship_manager = ShipManager(event = event)
        storage.storage_dict["MainGameManager"].game_event_manager()

        player_fire_animation_widget = FireAnimationWidget()

        storage.storage_dict["radio_animation"].show()

        shield_widget = ShieldWidget()

        turn_label = PygameLabel(
            path = "static/images/blue_button.png",
            coordinates = (500, 10),
            size = (128*2, 32*2),
            text = (lambda: "your turn" if storage.storage_dict["player_turn"] else "enemy turn")(),
            font_size = 40,
            color = (lambda: (0, 255, 0) if storage.storage_dict["player_turn"] else (255, 0, 0))()
        )

        quest_label = QuestLabel(
            x = 800,
            y = 0,
            event = event,
        )

        ability_label = AbilityLabel(
            coordinates = (100, 60),
            event = event
        )