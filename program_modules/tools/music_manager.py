from pygame import mixer
from .search_path import search_path

class PygameMusic():
    def __init__(self, path : str, volume : int):
        self.music = mixer.music
        self.music.load(search_path(path))
        self.music.set_volume(volume)
    
    def play(self, loops : int = 0):
        self.music.play(loops = loops)

class MusicManager():
    def __init__(self):
        mixer.init()
        self.volume = 1.0

        self.music_dict = {
            "kill_effect": PygameMusic("static/sound/effects/kill.mp3", self.volume*0.1),
            "hit_effect": PygameMusic("static/sound/effects/hit.mp3", self.volume*0.1),
            "shield1": PygameMusic("static/sound/effects/shield1.mp3", self.volume*0.1),
            "shield2": PygameMusic("static/sound/effects/shield2.mp3", self.volume*0.1),
            "shield4": PygameMusic("static/sound/effects/shield4.mp3", self.volume*0.1)
        }

music_manager = MusicManager()