# create pygame screen 1200X900
import pygame

def start_game():
    pygame.init()
    game = True
    screen = pygame.display.set_mode(size = (800, 600))

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
        pygame.display.flip()

