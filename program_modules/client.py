import socket
from .pygame_storage import pygame_storage
import threading

class Client():
    def __init__(self, ip : str, port : int):
        self.client_socket = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)
        self.ip = ip    
        self.port = port
        self.get_data_func = threading.Thread(target = self.get_data)
        
        self.data = None
        self.listening = True
        
    def join(self):
        self.client_socket.connect((self.ip, self.port))

        player_type = self.client_socket.recv(1024).decode("utf-8")

        if player_type == "1":
            pygame_storage.add_variable({"number_client" : "1"})
        else:
            pygame_storage.add_variable({"number_client" : "2"})

        print(pygame_storage.storage_dict["number_client"])
                       
    def get_data(self):
        while self.listening:
            if self.ip != "" and self.port != 0:
                try:
                    data = self.client_socket.recv(1024)
                    if data:
                        self.data = data.decode("utf-8")
                except Exception as error:
                    print(error)

    def send_data(self, data : str):
        self.client_socket.sendall(data.encode("utf-8"))