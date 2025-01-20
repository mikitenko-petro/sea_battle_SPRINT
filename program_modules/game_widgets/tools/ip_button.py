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
            self,
            coordinates = coordinates,
            size = size,
            event = event,
            path = "static/images/ip_button.png",
            function = self.get_ip
        )
    
    def get_ip(self):
        storage.storage_dict['IP'] = socket.gethostbyname(socket.gethostname())