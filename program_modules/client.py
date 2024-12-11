import socket
from .pygame_storage import pygame_storage

class Client():
    def __init__(self, ip : str, port : int):
        self.client_socket = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)
        self.ip = ip    
        self.port = port
        
    def join(self):
        self.client_socket.connect((self.ip, self.port))

        player_type = self.client_socket.recv(1024).decode("utf-8")

        if player_type == "1":
            pygame_storage.add_variable({"number_client" : "1"})
        else:
            pygame_storage.add_variable({"number_client" : "2"})
                       
    def get_data(self):
        data = self.client_socket.recv(1024)
        if data:
            return data.decode("utf-8")

    def send_data(self, data : str):
        self.client_socket.sendall(data.encode("utf-8"))