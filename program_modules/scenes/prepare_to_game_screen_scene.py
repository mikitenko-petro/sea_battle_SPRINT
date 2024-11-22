import pygame
from ..widgets.pygame_image import PygameImage
from ..game_modules.grid import Grid


class PrepareToGameScreenScene():
    def __init__(self, screen):
        self.screen = screen
        self.prepare_grid = Grid()

    def run(self, event : object):
        background_image = PygameImage(
        screen = self.screen,
        path = "static/images/sea_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))

        cell_x = 0
        cell_y = 0

        for row in self.prepare_grid.grid:
                for column in row:
                    if column == '':
                        cell = PygameImage(
                            screen = self.screen,
                            path = "static/images/cell.png",
                            coordinates = (350 + cell_x, 150 + cell_y),
                            size = (50, 50))
                        
                    cell_x += 50
                cell_y += 50
                cell_x = 0

        for ship_x in range(4): 
            ship = PygameImage(
                coordinates = (500 + ship_x*50, 50),
                size = (50, 50),
                screen = self.screen,
                path ="static/images/ship1X1.png"
            )