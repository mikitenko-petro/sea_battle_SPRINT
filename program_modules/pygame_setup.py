import pygame
import sys
from .scene_manager import SceneManager
from .pygame_storage import PygameStorage
from .client import Client

#Робим класс гри
class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size = (1200, 700))
        self.pygame_storage = PygameStorage()
        self.client = Client(ip = "26.39.233.93", port = 0)
        self.scene_manager = SceneManager(screen = self.screen, pygame_storage = self.pygame_storage, client = self.client)
        

    #Робим клас запуску гри
    def run(self):
        game = True

        #Робим цикл
        while game:
            event = pygame.event.get()

            #робим ще один цикл
            for pygame_event in event:
                if pygame_event.type == pygame.QUIT:
                    game = False
                    sys.exit()

            self.scene_manager.show(event = event)

            pygame.display.update()
            pygame.display.flip()

#Метод для запуску гри
def start_game(): 
    game = Game()
    game.run()