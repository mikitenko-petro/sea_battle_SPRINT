import socket
from .tools.storage import storage
import threading

#Робимо клас для клієнта
class Client():
    def __init__(self):
        self.client_socket = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)

        self.ip = ""    
        self.port = 0
        self.get_data_func = threading.Thread(target = self.get_data)
        
        self.listening = True
        
    def join(self):
        self.client_socket.connect((self.ip, self.port))      
                       
    def get_data(self):
        while self.listening:
            if self.ip != "" and self.port != 0:
                try:
                    data = self.client_socket.recv(1024).decode("utf-8")
                    if data:
                        storage.storage_dict["DataManager"].load_data(data)
                except ConnectionAbortedError:
                    ...
                
                except Exception as error:
                    print(error)
                    
    def send_data(self, data : str):
        self.client_socket.sendall(data.encode("utf-8"))
