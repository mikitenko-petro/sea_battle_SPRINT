from ...tools.pygame_storage import pygame_storage
from ...tools.music_manager import music_manager

def check_hit_collision(row, column, enemy = True):
    if pygame_storage.storage_dict["PLAYER_GRID"].grid[row][column] == "~":
        if enemy:
            music_manager.music_dict["hit_effect"].play()

        print("hit")
        return "hit"
    
    elif pygame_storage.storage_dict["PLAYER_GRID"].grid[row][column] == "O":
        print("shield")
        return "shield"
        
    else:
        print("miss")
        return "miss"