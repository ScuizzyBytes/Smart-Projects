import socket
import threading

# Укажи IP-адрес друга (сервера)
HOST = '127.0.0.1'  # Замени на IP сервера (например '192.168.x.x' или внешне)
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("[+] Подключено к серверу! Можно писать сообщения.")

# Функция для непрерывного приема сообщений
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\n[Друг]: {message}\nВы: ", end='')
        except ConnectionResetError:
            print("\n[-] Соединение разорвано.")
            break

# Запускаем прием сообщений в отдельном потоке
threading.Thread(target=receive_messages, daemon=True).start()

# Главный цикл для отправки сообщений
while True:
    msg = input("Вы: ")
    if msg.lower() == 'exit':
        break
    client.send(msg.encode('utf-8'))

client.close()