import pygame

class Performer():
    def __init__(self, action_list):
        self.action_list = action_list

    def perform(self):
        for action in self.action_list:
            if action == action.draw():
                action.draw()