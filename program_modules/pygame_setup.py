# create pygame screen 800x600
import pygame
from .widgets.pygame_image import PygameImage

def start_game():
    pygame.init()
    game = True
    screen = pygame.display.set_mode(size = (800, 600))
    background_image = PygameImage(screen, "sea_battle_SPRINT/static/images/great_sea_battle_bg.png", (800, 600))
    pygame.display.update()


    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
        pygame.display.flip()

