import pygame
from .scenes.scene_manager import SceneManager

class Game():
    def __init__(self):
        self = pygame.init()
        game = True
        screen = pygame.display.set_mode(size = (1200, 700))

        while game:
            event = pygame.event.get()
            scene_manager = SceneManager(screen = screen, event = event)
            scene_manager.show(1)

            for pygame_event in event:
                if pygame_event.type == pygame.QUIT:
                    game = False

            pygame.display.update()
            pygame.display.flip()
        

def start_game(): 
    game = Game()

