import socket
import io

with socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM) as client_socket:
    client_socket.connect(("192.168.1.18", 8081))
    message = "gus2232"
    client_socket.sendall(message.encode('utf-8'))
    