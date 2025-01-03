import pygame
import sys
from .client import Client
from .tools.scene_manager import SceneManager
from .tools.image_container import ImageContainer
from .tools.pygame_storage import pygame_storage
from .tools.data_manager import DataManager
from .game_widgets.fps_counter import FpsCounter
from .game_modules.achievements.achievement_manager import AchievementManager

pygame.init()
pygame_storage.add_variable({"debug": False})

pygame_storage.add_variable({"SCREEN" : pygame.display.set_mode(size = (1200, 700))}) 
pygame_storage.add_variable({"ImageContainer" : ImageContainer()})
pygame_storage.add_variable({"Client" : Client()})
pygame_storage.add_variable({"SceneManager" : SceneManager()})
pygame_storage.add_variable({"DataManager" : DataManager()})
pygame_storage.add_variable({"AchievementManager": AchievementManager()})

pygame.display.set_caption('Great Sea Battle')
pygame.display.set_icon(pygame_storage.storage_dict["ImageContainer"].images["static/images/icon.png"])

pygame_storage.add_variable({"clock": pygame.time.Clock()})

def run():
    fps_counter = FpsCounter(x = 0, y = 0)
    #Робим цикл
    while True:
        #Отримуємо усі дії миші та клавіатури
        event = pygame.event.get()

        #робим ще один цикл
        for pygame_event in event:
            if pygame_event.type == pygame.QUIT:
                pygame_storage.storage_dict["Client"].listening = False
                pygame_storage.storage_dict["Client"].client_socket.close()
                sys.exit()

        pygame_storage.storage_dict["SceneManager"].show(event = event)

        try:
            pygame_storage.storage_dict["AchievementManager"].check_all_achievements()
        except:
            pass

        fps_counter.render()

        pygame.display.update()
        pygame.display.flip()
        pygame_storage.storage_dict["clock"].tick(60)
