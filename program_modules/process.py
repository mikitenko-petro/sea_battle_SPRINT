import threading
from .pygame_setup import start_game
#from ..Serverserver.server import start_server

game = threading.Thread(target = start_game)
#server = threading.Thread(target = start_server)

game.start()
#server.start()

game.join()
#server.join()