import socket
import threading

class EchoServerThread(threading.Thread):
    def __init__(self, client_socket, logins):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.logins = logins

    def run(self):
        thread_name = threading.current_thread().name
        print("Wątek", thread_name, "- Nadeszło połączenie...")
        print("Wątek", thread_name, "- Parametry połączenia:", self.client_socket)
        while True:
            try:
                data = self.client_socket.recv(1024).decode("utf-8")
                if not data:
                    break
                print("Wątek", thread_name, "- Otrzymano:", data)
            except socket.error as e:
                print("Wątek", thread_name, "- Błąd wejścia-wyjścia:", e)
                break
        self.client_socket.close()

def main():
    logins = [
        ["adam123", "pass123", "Adam"],
        ["dama123", "pass123", "Dama"]
    ]

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5004))
    server_socket.listen(5)

    print("Inicjalizacja gniazda zakończona...")
    print("Parametry gniazda:", server_socket)

    while True:
        client_socket, _ = server_socket.accept()
        new_thread = EchoServerThread(client_socket, logins)
        new_thread.start()

if __name__ == "__main__":
    main()
