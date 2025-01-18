import socket
from ...tools.storage import storage
from ...widgets.pygame_button import PygameButton

class IpButton(PygameButton):
    def __init__(
            self,
            coordinates : tuple,
            size : tuple,
            event : object,
            path : str):
        
        PygameButton.__init__(
            coordinates = coordinates,
            size = size,
            event = event,
            path = path,
            function = None
        )
    
    def get_ip():
        storage.storage_dict['IP'] = socket.gethostbyname(socket.gethostname())