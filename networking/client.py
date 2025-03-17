import socket
import threading

class GameClient:
    def __init__(self, host='127.0.0.1', port=4455):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to {self.host}:{self.port}")
        threading.Thread(target=self.receive_messages).start()

    def send_message(self, message):
        self.client_socket.send(message.encode())

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                print(f"Received: {message}")
            except:
                break

if __name__ == "__main__":
    client = GameClient()
    client.connect()
    client.send_message("Hello from client")
