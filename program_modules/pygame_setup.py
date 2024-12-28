import pygame
import sys
from .tools.scene_manager import SceneManager
from .game_widgets.fps_counter import FpsCounter
from .tools.pygame_storage import pygame_storage
from .client import Client
from .tools.image_container import ImageContainer

#Робим класс гри
class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size = (1200, 700))
        self.client = Client(ip = "", port = 0)
        
        self.scene_manager = SceneManager(screen = self.screen, client = self.client)
        self.image_container = ImageContainer()
        
        pygame_storage.add_variable({"debug": False})
        self.fps_counter = FpsCounter(screen = self.screen, x = 0, y = 0)

    #Робим клас запуску гри
    def run(self):
        #Робим цикл
        while True:
            #Отримуємо усі дії миші та клавіатури
            event = pygame.event.get()

            #робим ще один цикл
            for pygame_event in event:
                if pygame_event.type == pygame.QUIT:
                    self.client.listening = False
                    self.client.client_socket.close()
                    sys.exit()

            self.scene_manager.show(event = event)

            self.fps_counter.render()

            pygame.display.update()
            pygame.display.flip()
            self.fps_counter.clock.tick(60)

pygame_storage.add_variable({"GAME": Game()})
#Метод для запуску гри
def start_game():
    pygame_storage.storage_dict["GAME"].run()