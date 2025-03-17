import socket
import threading

class GameClient:
    """
    Класс, представляющий клиента игры, который подключается к серверу для обмена сообщениями.

    Атрибуты:
        host (str): IP-адрес хоста, к которому будет подключаться клиент (по умолчанию '127.0.0.1').
        port (int): Порт, который будет использоваться для подключения (по умолчанию 4455).
        client_socket (socket.socket): Сокет, используемый для соединения с сервером.

    Методы:
        connect(): Подключается к серверу по указанному хосту и порту.
        send_message(message): Отправляет сообщение на сервер.
        receive_messages(): Получает и выводит сообщения от сервера.
    """

    def __init__(self, host='127.0.0.1', port=4455):
        """
        Инициализация клиента с указанным хостом и портом.

        Аргументы:
            host (str): IP-адрес хоста для подключения (по умолчанию '127.0.0.1').
            port (int): Порт для подключения (по умолчанию 4455).
        """
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Подключение клиента к серверу. После подключения запускается отдельный поток для получения сообщений.
        """
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to {self.host}:{self.port}")
        threading.Thread(target=self.receive_messages).start()

    def send_message(self, message):
        """
        Отправка сообщения на сервер.

        Аргументы:
            message (str): Сообщение, которое нужно отправить.
        """
        self.client_socket.send(message.encode())

    def receive_messages(self):
        """
        Получение сообщений от сервера. Сообщения выводятся в консоль.

        Если возникает ошибка при получении сообщения (например, соединение разорвано), поток завершает работу.
        """
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
