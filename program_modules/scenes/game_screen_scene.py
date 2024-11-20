import pygame
from ..widgets.pygame_image import PygameImage
from ..game_modules.grid import Grid

class GameScreneScene():
    def __init__(self, screen : object, scene_manager : object):
        self.screen = screen
        self.scene_manager = scene_manager
        self.grid = Grid()

    def run(self, event : object):
        background_image = PygameImage(
        screen = self.screen,
        path = "static/images/sea_bg.png",
        coordinates = (0, 0),
        size = (1200, 700))

        cell_x = 0
        cell_y = 0

        for row in self.grid.grid:
            for column in row:
                if column == '':
                    cell = PygameImage(
                        screen = self.screen,
                        path = "static/images/cell.png",
                        coordinates = (50 + cell_x, 150 + cell_y),
                        size = (50, 50))
                    
                cell_x += 50
            cell_y += 50
            cell_x = 0