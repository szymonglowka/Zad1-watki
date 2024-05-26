import socket
import threading

class EchoServerThread(threading.Thread):
    def __init__(self, client_socket, logins):
        super().__init__()
        self.socket = client_socket
        self.logins = logins

    def run(self):
        thread_name = threading.currentThread().getName()

        try:
            brinp = self.socket.makefile('r')
            out = self.socket.makefile('w')

            while True:
                line = brinp.readline().strip()
                print(thread_name + "| Line read: " + line)

                # Implementacja logiki serwera...

        except Exception as e:
            print(thread_name + "| Input/output error: " + str(e))

        finally:
            self.socket.close()

# Inicjalizacja listy użytkowników
logins = [
    ["adam123", "pass123", "Adam"],
    ["dama123", "pass123", "Dama"]
]

# Inicjalizacja gniazda serwera
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 7001))
server_socket.listen(5)

print("Inicjalizacja gniazda zakończona...")
print("Parametry gniazda: ", server_socket)

# Główna pętla serwera
while True:
    try:
        client_socket, _ = server_socket.accept()
        print("Nadeszło połączenie...")
        print("Parametry połączenia: ", client_socket)
        thread = EchoServerThread(client_socket, logins)
        thread.start()
    except Exception as e:
        print("Błąd wejścia-wyjścia: ", e)
