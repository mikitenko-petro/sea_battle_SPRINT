import socket
import pickle
import io
import os

sea = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]]

def start_server():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("SERVER_IP", 8081))
        #Переводить socket в режим очікування
        
        
        server_socket.listen()
        print("connecting ... ")
        # Очікує та приймає підключення клієнту
        client_socket, adress = server_socket.accept()
        print("connected", adress)
        while True:
            data = client_socket.recv(4096)
            #message = str(sea)
            #if input('Go?') == "yes":
            #    server_socket.sendall(message.encode('utf-8'))  
            if data:
                print(pickle.loads(data))
start_server()