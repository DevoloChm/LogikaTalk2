import socket
import threading

HOST = '0.0.0.0'
PORT = 0000
clients = []
def broadcast(data, exclude_socket=None):
    for client in clients:
        if client != exclude_socket:
            try:
                client.sendal(data)
            except:
                pass

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(4096)
            if not data:
                break
                broadcast(data, exclude_socket=client_socket)
        except:
            break
    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()

def main():
    server