import socket
import threading

# Настройки подключения
HOST = '0.0.0.0'  # Слушать все входящие адреса
PORT = 5000       # Порт для подключения

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[+] Сервер запущен на порту {PORT}. Ожидание друга...")
conn, addr = server.accept()
print(f"[+] Друг подключился с адреса: {addr}")

# Функция для непрерывного приема сообщений
def receive_messages():
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\n[Друг]: {message}\nВы: ", end='')
        except ConnectionResetError:
            print("\n[-] Друг отключился.")
            break

# Запускаем прием сообщений в отдельном потоке
threading.Thread(target=receive_messages, daemon=True).start()

# Главный цикл для отправки сообщений
while True:
    msg = input("Вы: ")
    if msg.lower() == 'exit':
        break
    conn.send(msg.encode('utf-8'))

conn.close()