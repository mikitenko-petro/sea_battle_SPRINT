import pygame
import sys
from .scene_manager import SceneManager
from .pygame_storage import pygame_storage
from .client import Client

#Робим класс гри
class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size = (1200, 700))
        self.client = Client(ip = "", port = 0)
        
        self.scene_manager = SceneManager(screen = self.screen, client = self.client)
        
        pygame_storage.add_variable({"debug": False})

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

            pygame.display.update()
            pygame.display.flip()

pygame_storage.add_variable({"GAME": Game()})
#Метод для запуску гри
def start_game():
    pygame_storage.storage_dict["GAME"].run()