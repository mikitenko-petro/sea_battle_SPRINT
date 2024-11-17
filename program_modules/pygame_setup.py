import pygame
from .scenes.main_screen_scene import MainScreenScene
from .scenes.game_screen_scene import GameScreneScene

class Game():
    def __init__(self):
        self = pygame.init()
        game = True
        screen = pygame.display.set_mode(size = (1200, 700))

        while game:
            event = pygame.event.get()
            main_screen = MainScreenScene(screen, event)
            # game_screen = GameScreneScene(screen)

            for pygame_event in event:
                if pygame_event.type == pygame.QUIT:
                    game = False

            pygame.display.update()
            pygame.display.flip()
        

def start_game(): 
    game = Game()

