from ..tools.storage import storage
from ..tools.music_manager import music_manager
from ..widgets.pygame_image import PygameImage
from ..widgets.pygame_text import PygameText
from ..widgets.pygame_animation import PygameAnimation
import threading
import time

class WaitingRoomScreenScene():
    def __init__(self):
        self.waiting_active = True
        self.waiting_thread = None
        self.anim_thread = None

    def run(self, event):
        background_image = PygameImage(
            path="static/images/sea_bg.png",
            coordinates=(0, 0),
            size=(1200, 700)
        )

        title_text = PygameText(
            text="waiting for opponent",
            font="static/fonts/alagard.ttf",
            font_size=100,
            x=100,
            y=500,
        )

        storage.add_variable({"loading_animation":
            PygameAnimation(
                animation_name="loading",
                coordinates=(550, 325),
                size=(100, 25),
                speed=0.1
            )
        })

        storage.storage_dict["Client"].send_data("Joined")
        self.start_threads()

    def move_from_wait(self):
        start_time = time.time()
        timeout = 30
        try:
            while self.waiting_active:
                if time.time() - start_time > timeout:
                    self.waiting_active = False
                    break

                data = storage.storage_dict["Client"].get_data2()
                if data == "Joined":
                    storage.storage_dict["SceneManager"].change_scene(scene="game")
                    music_manager.music["background_music"].stop()
                    music_manager.music["battle_music"].play(loops=-1)
                    storage.storage_dict["Client"].send_data("Joined")
                    self.waiting_active = False
                    break
        except Exception as e:
            print(f"Error in move_from_wait: {e}")
        finally:
            print("Exiting waiting thread.")

    def start_threads(self):
        self.waiting_thread = threading.Thread(target=self.move_from_wait, daemon=True)
        self.waiting_thread.start()

        self.anim_thread = threading.Thread(
            target=storage.storage_dict["loading_animation"].display, daemon=True
        )
        self.anim_thread.start()

    def stop_threads(self):
        self.waiting_active = False
        if self.waiting_thread and self.waiting_thread.is_alive():
            self.waiting_thread.join()
        if self.anim_thread and self.anim_thread.is_alive():
            storage.storage_dict["loading_animation"].stop()
            self.anim_thread.join()
