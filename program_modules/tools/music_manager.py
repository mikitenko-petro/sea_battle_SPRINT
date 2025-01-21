from pygame import mixer
from .search_path import search_path

class MusicManager():
    def __init__(self):
        mixer.init()
        self.volume = 1.0

        self.sfx = {
            "kill_effect": mixer.Sound(search_path("static/sound/effects/kill.wav")),
            "hit_effect":  mixer.Sound(search_path("static/sound/effects/hit.wav")),
            "shield1": mixer.Sound(search_path("static/sound/effects/shield1.wav")),
            "shield2": mixer.Sound(search_path("static/sound/effects/shield2.wav")),
            "shield4": mixer.Sound(search_path("static/sound/effects/shield4.wav")),
            "radio_set": mixer.Sound(search_path("static/sound/effects/radio_set.wav")),
        }

        self.music = {
            "background_music": mixer.Sound(search_path("static/sound/music/background_music.wav")),
            "battle_music": mixer.Sound(search_path("static/sound/music/battle_music.wav"))
        }

        for sfx in self.sfx:
            self.sfx[sfx].set_volume(0.1*self.volume)
        
        for music in self.music:
            self.music[music].set_volume(0.1*self.volume)

music_manager = MusicManager()