import threading
from .pygame_setup import start_game
from .server import start_server

game = threading.Thread(target = start_game)
server = threading.Thread(target = start_server)

game.start()
server.start()