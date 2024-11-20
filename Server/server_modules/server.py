import socket
import pickle
import io
import os

def start_server():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server_socket:
        # зв'язуємо socket з IP та портом
        server_socket.bind(("192.168.0.196", 8082))
        #Переводить socket в режим очікування
        server_socket.listen(2)
        print("connecting...")
        # Очікує та приймає підключення клієнту
        client_socket, adress = server_socket.accept()
        print("connected:", adress)
        client_socket2, adress2 = server_socket.accept()
        print("connected:", adress2)
        while True:
            data = client_socket.recv(1024)
            
            if data:
                client_socket2.sendall(data)
                print(f"send: {data}")

            data2 = client_socket2.recv(1024)

            if data2:
                client_socket.sendall(data2)
                print(f"send: {data2}")
start_server()