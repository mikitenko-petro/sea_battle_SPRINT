from pygame import mixer
from .search_path import search_path

class PygameMusic():
    def __init__(self, path : str, volume : int):
        self.music = mixer.music
        self.music.load(search_path(path))
        self.music.set_volume(volume)
    
    def play(self, loops : int = 1):
        self.music.play(loops = loops)

class MusicManager():
    def __init__(self):
        mixer.init()
        self.volume = 1.0

        self.music_dict = {
            "hit_effect" : PygameMusic("static/sound/effects/hit.mp3", self.volume*0.1),
            "kill_effect" : PygameMusic("static/sound/effects/kill.mp3", self.volume*0.1),
        }

music_manager = MusicManager()