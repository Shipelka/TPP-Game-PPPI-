import socket
import threading

class GameServer:
    def __init__(self, host='127.0.0.1', port=4455):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_sockets = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")
            self.client_sockets.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                if not message:
                    break
                # Process message (game state, player actions, etc.)
                self.broadcast(message, client_socket)
            except:
                break
        client_socket.close()
        self.client_sockets.remove(client_socket)

    def broadcast(self, message, sender_socket):
        for client_socket in self.client_sockets:
            if client_socket != sender_socket:
                client_socket.send(message)

if __name__ == "__main__":
    server = GameServer()
    server.start()
