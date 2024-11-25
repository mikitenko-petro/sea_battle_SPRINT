import pygame
from .scenes.scene_manager import SceneManager
from .pygame_storage import PygameStorage

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size = (1200, 700))
        self.pygame_storage = PygameStorage()
        self.scene_manager = SceneManager(screen = self.screen, pygame_storage = self.pygame_storage)

    def run(self):
        game = True

        while game:
            event = pygame.event.get()

            self.scene_manager.show(event = event)

            for pygame_event in event:
                if pygame_event.type == pygame.QUIT:
                    game = False

            pygame.display.update()
            pygame.display.flip()
        
def start_game(): 
    game = Game()
    game.run()