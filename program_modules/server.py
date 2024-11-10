import socket
import io
import os

def start_server():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("192.168.1.18", 8081))
        #Переводить socket в режим очікування
        
        while True:
            server_socket.listen()

            print("connecting ... ")
            # Очікує та приймає підключення клієнту
            client_socket, adress = server_socket.accept()

            print("connected", adress)

            data = client_socket.recv(1024)

            if data:
                print(data.decode('utf-8'))