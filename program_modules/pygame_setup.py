import pygame
import sys
from .tools.storage import storage
from .client import Client
from .tools.scene_manager import SceneManager
from .tools.image_container import ImageContainer
from .game_modules.main_game_manager import MainGameManager
from .tools.data_manager import DataManager
from .game_widgets.tools.fps_counter import FpsCounter
from .game_modules.achievements.achievement_manager import AchievementManager
from .game_modules.stats.stats_manager import StatsManager
from .game_modules.abilites.ability_manager import AbilityManager

pygame.init()
storage.add_variable({"debug": False})

storage.add_variable({"SCREEN" : pygame.display.set_mode(size = (1200, 700))}) 
storage.add_variable({"ImageContainer" : ImageContainer()})
storage.add_variable({"Client" : Client()})
storage.add_variable({"SceneManager" : SceneManager()})
storage.add_variable({"DataManager" : DataManager()})
storage.add_variable({"AchievementManager": AchievementManager()})
storage.add_variable({"MainGameManager" : MainGameManager()})
storage.add_variable({"StatsManager" : StatsManager()})
storage.add_variable({"AbilityManager" : AbilityManager()})
storage.add_variable({"destroed_4x1_ships" : 0})

pygame.display.set_caption('Great Sea Battle')
pygame.display.set_icon(storage.storage_dict["ImageContainer"].images["static/images/icon.png"])

storage.add_variable({"clock": pygame.time.Clock()})

def run():
    fps_counter = FpsCounter(x = 0, y = 0)
    storage.storage_dict["AchievementManager"].load_achievements()
    storage.storage_dict["StatsManager"].load_stats()

    while True:
        event = pygame.event.get()

        for pygame_event in event:
            if pygame_event.type == pygame.QUIT:
                # storage.storage_dict["Client"].send_data("Close server")
                storage.storage_dict["Client"].listening = False
                storage.storage_dict["Client"].client_socket.close()
                sys.exit()

        storage.storage_dict["SceneManager"].show(event = event)

        storage.storage_dict["AchievementManager"].check_all_achievements()
        storage.storage_dict["StatsManager"].save_stats()
        storage.storage_dict["AchievementManager"].check_unlocks()

        fps_counter.render()

        pygame.display.update()
        pygame.display.flip()
        storage.storage_dict["clock"].tick(60)