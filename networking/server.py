import socket
import threading


class GameServer:
    """
    Класс, представляющий сервер игры, который принимает подключения от клиентов и обмениваться с ними сообщениями.

    Атрибуты:
        host (str): IP-адрес хоста для запуска сервера (по умолчанию '127.0.0.1').
        port (int): Порт для прослушивания входящих подключений (по умолчанию 4455).
        server_socket (socket.socket): Сокет сервера для прослушивания входящих подключений.
        client_sockets (list): Список всех подключенных клиентских сокетов.

    Методы:
        start(): Запускает сервер, который ожидает подключения клиентов.
        handle_client(client_socket): Обрабатывает взаимодействие с каждым клиентом, получает и передает сообщения.
        broadcast(message, sender_socket): Отправляет сообщение всем клиентам, кроме отправителя.
    """

    def __init__(self, host='127.0.0.1', port=4455):
        """
        Инициализация сервера с указанным хостом и портом.

        Аргументы:
            host (str): IP-адрес хоста для подключения (по умолчанию '127.0.0.1').
            port (int): Порт для подключения (по умолчанию 4455).
        """
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_sockets = []

    def start(self):
        """
        Запуск сервера, который привязывается к указанному хосту и порту, затем начинает слушать подключения.
        После подключения клиента создается новый поток для обработки этого клиента.
        """
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")
            self.client_sockets.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        """
        Обработка каждого клиента: получение сообщений и передача их другим клиентам.

        Аргументы:
            client_socket (socket.socket): Сокет клиента, с которым сервер взаимодействует.
        """
        while True:
            try:
                message = client_socket.recv(1024)
                if not message:
                    break
                # Обработка полученного сообщения (состояние игры, действия игроков и т.д.)
                self.broadcast(message, client_socket)
            except:
                break
        client_socket.close()
        self.client_sockets.remove(client_socket)

    def broadcast(self, message, sender_socket):
        """
        Отправка сообщения всем клиентам, кроме отправителя.

        Аргументы:
            message (str): Сообщение, которое нужно отправить.
            sender_socket (socket.socket): Сокет клиента, который отправил сообщение.
        """
        for client_socket in self.client_sockets:
            if client_socket != sender_socket:
                client_socket.send(message)


if __name__ == "__main__":
    server = GameServer()
    server.start()
