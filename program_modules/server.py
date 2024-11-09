import socket
from threading import Thread
import io
import os

def start_server():
    with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("SERVER_IP", 8081))
        server_socket.listen()
        client_socket, adress = server_socket.accept()
        print("connected to", adress)
        data = client_socket.recv(1024)
        if data:
            print(data.decode('utf-8'))           

server_therd = Thread(target= start_server)
server_therd.start()
print("Done")